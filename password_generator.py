import random

characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()-=_+?><,./;:|]}[{"

while True:
    pwd_len = int(input("Length of the Password: "))
    pwd_count = int(input("How many Passwords?: "))

    for x in range(0, pwd_count):
        pwd = ""
        for x in range(0, pwd_len):
            pwd_char = random.choice(characters)
            pwd = pwd + pwd_char
        print("Your Password: " + pwd)
        