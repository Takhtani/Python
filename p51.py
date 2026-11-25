import subprocess
import platform

ip_list = ["127.0.0.1", "127.0.0.2", "203.0.113.5"]

# Windows uses -n for count, Linux/Mac use -c
param = "-n" if platform.system().lower() == "windows" else "-c"

print("Ping scan started...\n")
for ip in ip_list:
    result = subprocess.run(["ping", param, "1", ip],
                            stdout=subprocess.DEVNULL,
                            stderr=subprocess.DEVNULL,
                            timeout=10)
    if result.returncode == 0:
        print(f"{ip:15} is UP")
    else:
        print(f"{ip:15} is DOWN")
