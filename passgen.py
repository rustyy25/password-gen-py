import random
import time
import string

letters = string.ascii_letters
digits = string.digits
symbols = string.punctuation

length = int(input("Provide a length: "));
chars = letters + digits + symbols
password = "";

def Wait():
    for _ in range(3):
        print("Generating your password...")
        time.sleep(1)

for i in range(length):
    password = password + random.choice(chars);

Wait()
print(f'Your new password is: {password}')
