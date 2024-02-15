import nmap

def port_scanner_nmap(target_ip, ports):


    scanner = nmap.PortScanner()
    scan_info = scanner.scan(target_ip, ports)

    open_ports = {}
    for host, scan_data in scan_info['scan'].items():
        for port, port_data in scan_data['tcp'].items():
            if port_data['state'] == 'open':
                service = port_data.get('product', 'service')
                open_ports[port] = service or "Unknown"

    return open_ports

# Example usage:
target_ip = "192.168.1.100"
ports = "22,80,443"

open_ports = port_scanner_nmap(target_ip, ports)

if open_ports:
    print("Open ports:")
    for port, service in open_ports.items():
        print(f"  - {port}: {service}")
else:
    print("No open ports found in the specified range.")
