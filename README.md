# Basic Port Scanner

A simple Python-based TCP port scanner that can scan a single port or a range of ports on a given IP address.  
This project is intended for **educational purposes** and ethical security testing only.

---

## Features
- Scan a single TCP port.
- Scan a range of TCP ports.
- Simple and lightweight.
- Written in Python 3 with the `socket` module.

---

## Usage

### Scan a single port
```bash
# Syntax
python3 src/main.py <IP> <PORT>

# Example
python3 src/main.py 127.0.0.1 80
```
## New CLI (argparse)
```bash
# Single port
python3 src/main.py --ip 127.0.0.1 --port 80

# Range (inclusive)
python3 src/main.py --ip 127.0.0.1 --range 20 100

# Help
python3 src/main.py -h
```

---

## Example Output
[*] Scanning ports 20 to 25 on 127.0.0.1
[-] Port 20 is closed
[-] Port 21 is closed
[+] Port 22 is open
[-] Port 23 is closed
[+] Port 25 is open

---

## Requirements
- Python 3.x
- Works on Linux, macOS, and Windows (but best tested on Kali Linux for security labs).

---

## Installation
Clone the repository and navigate into the project directory:

git clone https://github.com/<your-username>/basic-port-scanner.git 
cd basic-port-scanner

---

## Disclaimer
This tool is for educational purposes only.
Do NOT scan networks or devices without explicit permission.
The author is not responsible for any misuse of this tool.
