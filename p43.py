import whois

domain = input("Enter a domain name (e.g. google.com): ").strip()

try:
    info = whois.whois(domain)
    if not info.domain_name:
        print("No WHOIS information found for", domain)
    else:
        created = info.creation_date
        if isinstance(created, list):
            created = created[0]
        print("\nBasic WHOIS information")
        print("-" * 30)
        print("Domain     :", domain)
        print("Registrar  :", info.registrar)
        print("Created on :", created)
        print("Country    :", info.country)
except Exception as e:
    print("Lookup failed:", e)
