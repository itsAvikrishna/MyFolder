import random

print("PROJECT RPG ")
print()

print("Welcome to Random Password Generator")
print()

passwordchar = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789@#$&%"

nofpassword = int(input("Enter the number of password you want: "))
passlen = int(input("Enter a length of password: "))

print()
print("Here are some random passwords ")
print()

for i in range(nofpassword):
    password = ""
    for j in range(passlen):
        password = password + random.choice(passwordchar)
    print(password)
    
print()
print("These are some random password")
