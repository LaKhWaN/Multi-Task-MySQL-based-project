import random

def hashing(hahsed_pass=None):
    password = input("Please enter your desired password here: ")
    if len(password) > 26:
        print("Password is too long.")
        hashing()
    elif len(password) < 6:
        print("Password is too short.")
        hashing()
    choice = "abcdefghijklmnopqrstuvwxy1234567890!@~#$%^&*()-_=+"
    list2 = list(choice)
    list1 = list(password)
    length = len(list1)
    hashed_pass = ""
    for i in range(length):
        hashed_pass += list1[i]
        for h in range(3):
            hashed_pass+=random.choice(choice)
    return hashed_pass


def unhash(hashed_pass):
    unhash_pass = ""
    list3 = list(hashed_pass)
    length1 = len(list3)
    for i in range(0,length1,4):
        unhash_pass+=list3[i]
    return unhash_pass
