import random

chars ="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()"

while 1:
    password_len = int(input("Enter the length of the password: "))
    password =""
    for x in range(0,password_len):
        password_char = random.choice(chars)
        password = password + password_char
    print("Here is your password: ", password)