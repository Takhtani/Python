# identify suspicius keywords in the URL

url  = input("Enter a URL :  ")
words = ["login","verify","Bank","free","password"]
url = url.lower()

found = False

for word in words:
    if word in url:
        print("Suspicious keyword found : ", word)
        found = True
         print("URL NEEDS FURTHER INSPECTION !!!")
    else:
            print("NO LISTED SUSPICIUS WORD FOUNDED :)")
    
