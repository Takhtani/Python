# write a python program to genrate a rendom password

import random

char = "abcdefghIJKLMAFJSDVDSFNVDBDNjnvdnvdvdkv@154544655$"

password = ""

for i in range (8):
    password = password + random.choice(char)

print ("Generated password : ",password)
