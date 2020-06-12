import socket
import time
import sys
import argparse

def usage():
    print("[*] Usage:\npython3 portscan.py <arguments>")
    print("-t (--target):           specify the target to scan")
    print("-b (--begin):            specify the begin port")
    print("-e (--end):              specify the end port")
    print("-p (--port):             single port scan (do not use -b and -e with -p)")
    print("-d (--delay) [optional]: specify the max timeout")

def portscan(host : str, begin_port : int, end_port : int, delay : float):
    sdelay = 0.75
    bcounter = time.perf_counter()
    print("<< portscan.py by rdbo >>")
    time.sleep(sdelay)
    print(f"[*] Target: {host}")
    time.sleep(sdelay)
    print(f"[*] Scan range: {begin_port}-{end_port}")
    time.sleep(sdelay)
    print(f"[*] Max timeout: {delay}")
    time.sleep(sdelay)
    print("--------------------")
    time.sleep(0.5)
    open_ports = []
    for port in range(begin_port, end_port+1):
        print(f"[*] Scanning port {port}...")
        try:
            socket.setdefaulttimeout(delay)
            soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            out = soc.connect_ex((host, port))
            if(out == 0):
                open_ports.append(port)
        except KeyboardInterrupt:
            print()
            print("[!] KeyboardInterrupt, exiting...")
            break
        except:
            print(f"[!] Exception raised while connecting to {host}:{port}")
    
    ecounter = time.perf_counter()
    scan_time = round(ecounter - bcounter, 2)
    print("--------------------")
    print(f"[*] Scan finished in {scan_time} second(s)")
    print(f"[*] Open port(s): {[port for port in open_ports]}")


if (__name__ == "__main__"):
    parser = argparse.ArgumentParser()
    parser.add_argument("-t", "--target", action="store", dest="target", help="target", type=str, default="")
    parser.add_argument("-b", "--begin", action="store", dest="begin", help="begin port", type=int, default="-1")
    parser.add_argument("-e", "--end", action="store", dest="end", help="end port", type=int, default="-1")
    parser.add_argument("-p", "--port", action="store", dest="port", help="single port scan", type=int, default="-1")
    parser.add_argument("-d", "--delay", action="store", dest="delay", help="max timeout", type=float, default="1")
    args = parser.parse_args()
    try:
        host = str(args.target)
        bport = int(args.begin)
        eport = int(args.end)
        port = int(args.port)
        max_timeout = int(args.delay)
        if(len(host) > 0 and bport > -1 and eport > -1 and max_timeout > -1 and port == -1):
            portscan(str(host), int(bport), int(eport), float(max_timeout))
        elif(len(host) > 0 and bport == -1 and eport == -1 and max_timeout > -1 and port != -1):
            portscan(str(host), int(port), int(port), float(max_timeout))
        else:
            usage()


    except:
        print("[!] Unable to parse arguments.")
        usage()