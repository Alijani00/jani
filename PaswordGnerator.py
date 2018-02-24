import random
import string
string.ascii_lowercase
string.ascii_uppercase
char='abcdefghijklmnopqrstuvwxyz0123456789'


len=input('Input Length of Password :')
len=int(len)
number_of_password=input("Number_of_password: ")
number_of_password=int(number_of_password)
for p in range(number_of_password):
    password=''
    for a in range(len):
     #password += random.choice(string.ascii_uppercase)
     password += random.choice(char)
    print(password)


