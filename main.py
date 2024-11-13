import random
import string

letters = string.ascii_letters
digits = string.digits
symbols = string.punctuation

length = int(input("Provide a length: "))
amount = int(input("Enter the amount of password to generate: "))
chars = letters + digits + symbols

for i in range(amount):
    pwd = ""

    for j in range(length):
        pwd += random.choice(chars)
        
    print(f'Your new password is: {pwd}')