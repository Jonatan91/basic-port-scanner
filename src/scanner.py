import socket

"""
Scanner module: functions to scan a single TCP port and a range of ports.
All functions return simple Python types, suitable for CLI usage.
"""

def scan_single_port(ip, port):
    """
    Scans a single TCP port on a given IP address.
    Returns True if the port is open, False otherwise.
    """
    try:
        # Create a TCP socket
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # Set a timeout of 1 second
        s.settimeout(1)
        # Try to connect to the target IP and port
        result = s.connect_ex((ip, port))
        # Close the socket
        s.close()

        if result == 0:
            return True  # Port is open
        else:
            return False  # Port is closed
    except:
        # If any error occurs, consider the port closed
        return False


def scan_multiple_ports(ip, start_port, end_port):
    """
    Scans a range of TCP ports on a given IP address.
    Returns a list of open ports.
    """
    open_ports = []

    # Iterate through the port range
    for port in range(start_port, end_port + 1):
        if scan_single_port(ip, port):
            print(f"[+] Port {port} is open")
            open_ports.append(port)
        else:
            print(f"[-] Port {port} is closed")

    return open_ports
