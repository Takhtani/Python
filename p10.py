def string_length(s):
    return len(s)

def to_upper(s):
    return s.upper()

def to_lower(s):
    return s.lower()

def reverse_string(s):
    return s[::-1]

def count_vowels(s):
    return sum(1 for ch in s.lower() if ch in "aeiou")

def is_palindrome(s):
    s = s.replace(" ", "").lower()
    return s == s[::-1]

def replace_word(s, old, new):
    return s.replace(old, new)

def split_words(s):
    return s.split()

text = input("Enter a string: ")

print("Length            :", string_length(text))
print("Uppercase         :", to_upper(text))
print("Lowercase         :", to_lower(text))
print("Reversed          :", reverse_string(text))
print("Number of vowels  :", count_vowels(text))
print("Is palindrome?    :", is_palindrome(text))
print("After replace     :", replace_word(text, "University", "Group"))
print("Words in the text :", split_words(text))
print("Title case        :", text.title())
