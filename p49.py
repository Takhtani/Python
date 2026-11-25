import hashlib

text = input("Enter a string: ")
data = text.encode()

print("\nMD5     :", hashlib.md5(data).hexdigest())
print("SHA-1   :", hashlib.sha1(data).hexdigest())
print("SHA-256 :", hashlib.sha256(data).hexdigest())
print("SHA-512 :", hashlib.sha512(data).hexdigest())

# the same input always gives the same hash; a small change gives a different hash
print("\nSHA-256 of 'marwadi@2026':", hashlib.sha256(b"marwadi@2026").hexdigest())
