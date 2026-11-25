import subprocess
import socket

domain = input("Enter domain name: ")

print("\nIP address (socket):", socket.gethostbyname(domain))

for record in ["A", "NS", "MX"]:
    print(f"\n--- dig +short {domain} {record} ---")
    result = subprocess.run(["dig", "+short", domain, record],
                            capture_output=True, text=True)
    print(result.stdout.strip() or "No record found")
