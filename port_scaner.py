import socket

def port_scanner(target_ip, ports):


    open_ports = {}
    for port in ports:
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
                sock.settimeout(0.5)  # Set a timeout to avoid blocking
                result = sock.connect_ex((target_ip, port))
                if result == 0:
                    open_ports[port] = identify_service(target_ip, port)
                    sock.close()
        except OSError as e:
            print(f"Error scanning port {port}: {e}")

    return open_ports

def identify_service(target_ip, port):


    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        try:
            sock.connect((target_ip, port))
            data = sock.recv(1024).decode()  # Receive up to 1024 bytes of data
            return data.split()[0]  # Return the first word, assuming it's the service name
        except OSError:
            return "Unknown"

# Example usage:
target_ip = "192.168.1.100"
ports = range(22, 444)  # Scan ports 22-443

open_ports = port_scanner(target_ip, ports)

if open_ports:
    print("Open ports:")
    for port, service in open_ports.items():
        print(f"  - {port}: {service}")
else:
    print("No open ports found in the specified range.")
