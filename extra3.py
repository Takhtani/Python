# write a program to encode a message using base module and decode it

import base64

mess = input("Enter your Message :-")

data = mess.encode()

encode = base64.b64encode(data)

print("Encoded message :- " , encode.decode())

decoded = base64.b64decode(encode)

print("Decoded message :- " , decoded.decode())
