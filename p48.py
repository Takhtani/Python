import socket

host = input("Enter host/IP to scan: ")
start = int(input("Enter start port: "))
end = int(input("Enter end port: "))

print(f"\nScanning {host} from port {start} to {end} ...")
open_ports = []

for port in range(start, end + 1):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(0.5)
    result = s.connect_ex((host, port))       # 0 means connection succeeded
    if result == 0:
        print(f"Port {port}: OPEN")
        open_ports.append(port)
    else:
        print(f"Port {port}: closed")
    s.close()

print("\nOpen ports:", open_ports)
