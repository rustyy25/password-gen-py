import random
import time
import string

letters = string.ascii_letters
digits = string.digits
symbols = string.punctuation

length = int(input("Provide a length: "));
chars = letters + digits + symbols
password = "";

for i in range(length):
    password = password + random.choice(chars);
   
print('Generating your password...');
time.sleep(5);
print(f'Your new password is: {password}');
