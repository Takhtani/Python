import re

text = """Contact us at admin@marwadiuniversity.ac.in or support@example.com.
Invalid ones: user@@gmail.com, hello@.com, plainaddress.
Also try student.lab26@gmail.co.in for the lab."""

pattern = r"[A-Za-z0-9._%+-]+@[A-Za-z0-9-]+(?:\.[A-Za-z0-9-]+)*\.[A-Za-z]{2,}"

emails = re.findall(pattern, text)
print("Emails found in the text:")
for e in emails:
    print("  ", e)
print("Total:", len(emails))

print("\nValidating individual addresses:")
for addr in ["abc@gmail.com", "abc@gmail", "a.b@x.org", "@gmail.com"]:
    ok = re.fullmatch(pattern, addr) is not None
    print(f"  {addr:15} -> {'Valid' if ok else 'Invalid'}")
