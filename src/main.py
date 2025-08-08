import sys
from scanner import scan_single_port, scan_multiple_ports

if __name__ == "__main__":
    # If the user provides an IP and one port
    if len(sys.argv) == 3:
        ip = sys.argv[1]
        port = int(sys.argv[2])
        if scan_single_port(ip, port):
            print(f"[+] Port {port} is open on {ip}")
        else:
            print(f"[-] Port {port} is closed on {ip}")

    # If the user provides an IP and a range of ports
    elif len(sys.argv) == 4:
        ip = sys.argv[1]
        start_port = int(sys.argv[2])
        end_port = int(sys.argv[3])
        print(f"[*] Scanning ports {start_port} to {end_port} on {ip}")
        scan_multiple_ports(ip, start_port, end_port)

    # If the arguments are invalid, show usage instructions
    else:
        print("Usage:")
        print("  python3 main.py <IP> <PORT>")
        print("  python3 main.py <IP> <START_PORT> <END_PORT>")
