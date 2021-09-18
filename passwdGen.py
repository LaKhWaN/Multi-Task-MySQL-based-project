import random

def passwdGen():
    choices = "abcdefghijklmnopqrstuvwxyz1234567890!@#$%^&*()_+=-`~"
    n = random.randrange(10,24)
    passwd = ""
    for i in range(n):
        passwd+=random.choice(choices)
    print("Your randomly generated password is: "+passwd)