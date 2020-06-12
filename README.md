# portscanner.py
Simple python3 script for port scanning
```
[*] Usage:
python3 portscan.py <arguments>
-t (--target):           specify the target to scan
-b (--begin):            specify the begin port
-e (--end):              specify the end port
-p (--port):             single port scan (do not use -b and -e with -p)
-d (--delay) [optional]: specify the max timeout
```
Example:
```
$ python3 portscan.py -t duckduckgo.com -b 440 -e 450

<< portscan.py by rdbo >>
[*] Target: duckduckgo.com
[*] Scan range: 440-450
[*] Max timeout: 1.0
--------------------
[*] Scanning port 440...
[*] Scanning port 441...
[*] Scanning port 442...
[*] Scanning port 443...
[*] Scanning port 444...
[*] Scanning port 445...
[*] Scanning port 446...
[*] Scanning port 447...
[*] Scanning port 448...
[*] Scanning port 449...
[*] Scanning port 450...
--------------------
[*] Open ports: [443]
[*] Scan finished in 10.00 second(s)
```
