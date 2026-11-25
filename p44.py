import whois

domain = input("Enter domain name: ")
w = whois.whois(domain)
print("Registrar of", domain, "is:", w.registrar)
