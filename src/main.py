import argparse
import ipaddress
import time
from scanner import scan_single_port, scan_multiple_ports

def valid_port(value: str) -> int:
    """
    argparse validator to ensure the port is an integer in [1, 65535].
    """
    try:
        port = int(value)
    except ValueError:
        raise argparse.ArgumentTypeError("Port must be an integer")
    if not (1 <= port <= 65535):
        raise argparse.ArgumentTypeError("Port must be between 1 and 65535")
    return port

def parse_args():
    """
    Build and parse CLI arguments using argparse.
    Supports scanning one port (--port) or a range (--start --end).
    """
    parser = argparse.ArgumentParser(
        description="Basic TCP Port Scanner (education only)"
    )
    parser.add_argument("--ip", required=True, help="Target IP address (e.g., 127.0.0.1)")
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--port", type=valid_port, help="Single TCP port to scan")
    group.add_argument("--range", nargs=2, metavar=("START", "END"), type=valid_port,
                       help="Range of ports to scan (inclusive), e.g., 20 100")

    return parser.parse_args()

def validate_ip(ip_str: str) -> str:
    """
    Validate that the given string is a valid IPv4 address.
    Returns the normalized IP string or raises ValueError.
    """
    try:
        return str(ipaddress.IPv4Address(ip_str))
    except ipaddress.AddressValueError:
        raise ValueError("Invalid IPv4 address")

if __name__ == "__main__":
    args = parse_args()

    # Validate IP
    try:
        target_ip = validate_ip(args.ip)
    except ValueError as e:
        print(f"[!] {e}")
        exit(1)

    start_time = time.time()

    # Single port case
    if args.port is not None:
        is_open = scan_single_port(target_ip, args.port)
        if is_open:
            print(f"[+] Port {args.port} is open on {target_ip}")
        else:
            print(f"[-] Port {args.port} is closed on {target_ip}")
        scanned = 1
        open_ports = [args.port] if is_open else []

    # Range case
    else:
        start_port, end_port = args.range
        if start_port > end_port:
            print("[!] START must be <= END")
            exit(1)
        print(f"[*] Scanning ports {start_port} to {end_port} on {target_ip}")
        open_ports = scan_multiple_ports(target_ip, start_port, end_port)
        scanned = (end_port - start_port) + 1

    elapsed = time.time() - start_time
    # Summary
    print("\n=== Scan Summary ===")
    print(f"Target: {target_ip}")
    print(f"Ports scanned: {scanned}")
    print(f"Open ports: {', '.join(map(str, open_ports)) if open_ports else 'None'}")
    print(f"Elapsed time: {elapsed:.2f}s")
