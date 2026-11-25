import whois

def first(value):
    return value[0] if isinstance(value, list) else value

domain = input("Enter domain name: ")
result = whois.whois(domain)

print("\nWHOIS lookup result for", domain)
print("Domain name   :", first(result.domain_name))
print("Registrar     :", result.registrar)
print("WHOIS server  :", result.whois_server)
print("Creation date :", first(result.creation_date))
print("Name servers  :", ", ".join(sorted(set(n.upper() for n in result.name_servers))))
