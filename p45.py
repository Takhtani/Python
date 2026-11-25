import whois

domain = input("Enter domain name: ")
w = whois.whois(domain)

created = w.creation_date
if isinstance(created, list):          # some domains return a list of dates
    created = created[0]
print("Creation date of", domain, "is:", created)
