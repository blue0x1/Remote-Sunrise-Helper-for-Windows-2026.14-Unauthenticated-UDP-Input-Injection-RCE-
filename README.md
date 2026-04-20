# Remote Sunrise Helper for Windows 2026.14 - Unauthenticated UDP Input Injection (RCE)
Remote Sunrise Helper for Windows 2026.14 - Unauthenticated UDP Input Injection (RCE)

```
 
# Exploit Title: Remote Sunrise Helper for Windows 2026.14 - Unauthenticated UDP Input Injection (RCE)
# Date: 2026-04-20
# Exploit Author: Chokri Hammedi
# Software: https://rs.ltd/latest.php?os=win
# Vendor: https://rs.ltd/
# Version: 2026.14
# Tested on: Windows 10 / Windows 11
#
# Identification:
# nmap -p- -T4 <target> --script ssl-cert
# Look for SSL cert with subject: CN=SecureHTTPServer/O=Evgeny Cherpak/C=US
```

## syntax 
```
Usage: poc.py <target_ip> <port> <command>
Example: poc.py 192.168.1.103 49737 'calc'

```
<img width="513" height="90" alt="image" src="https://github.com/user-attachments/assets/ca1ece6d-6f4f-45d6-a72f-674805437a33" />

a cmd popup and executed the command "whoami"

<img width="535" height="181" alt="image" src="https://github.com/user-attachments/assets/141da16f-2ef3-4a93-8945-71f50acc2e38" />
