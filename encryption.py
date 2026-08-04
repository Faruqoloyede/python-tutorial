import random
import string

chars = " " + string.digits + string.punctuation + string.ascii_letters

chars = list(chars)
key = chars.copy()
random.shuffle(key)

text = input("Enter the text you want to encrypt: ")
cipher_text = ""

password = "faruq@"

for letter in text:
    index = chars.index(letter)
    cipher_text += key[index]
print(cipher_text)


cipher_text = input("Enter the text you want to decrypt: ")
text = ""

decrypt_password = input("Enter your password to decrypt: ")

if decrypt_password == password:
    for letter in cipher_text:
        index = key.index(letter)
        text += chars[index]
else:
    print("Wrong password")
print(text)