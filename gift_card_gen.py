# Gift card Generator:

# 1. Amazon Gift Card
# 2. Google Play store

import random

def amazon():
    time = int(input("How many amazon Gift Card would you like to generate?\n"))
    for a in range(time):
        choice1 = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        choice2 = "1234567890"
        number = ""
        for i in range(2):
            number+=random.choice(choice1)
        for i in range(2):
            number+=random.choice(choice2)
        number+="-"
        for i in range(2):
            number+=random.choice(choice1)
        for i in range(1):
            number+=random.choice(choice2)
        for i in range(3):
            number+=random.choice(choice1)
        number+="-"
        for i in range(1):
            number+=random.choice(choice1)
        for i in range(1):
            number+=random.choice(choice2)
        for i in range(2):
            number+=random.choice(choice1)
        for i in range(1):
            number+=random.choice(choice2)
        file = open("Amazon Gift Cards.txt","a")
        file.write(number + "\n")
        file.close()
        print('A file has been saved named as Amazon Gift cards.')

# Google Play Store:
def playstore():
    times = int(input("How many Gift card would you like to generate?\n"))
    for k in range(times):
        choice = "ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
        number = ""
        for i in range(4):
            number+=random.choice(choice)
        number+="-"
        for i in range(4):
            number+=random.choice(choice)
        number+="-"
        for i in range(4):
            number+=random.choice(choice)
        number+="-"
        for i in range(4):
            number+=random.choice(choice)
        number+="-"
        for i in range(4):
            number+=random.choice(choice)
        file = open("Google Play Store Gift Cards.txt","a")
        file.write(number + "\n")
        file.close()
        print('A file has been saved named as Google Play Store Gift Card.')
def start():
    print("Gift Card Generator: ")
    ask = input("What would you like to generate?\n\n1. Amazon Gift Card\n2. Google Play Store Gift Card\nEnter here: ")
    if ask == "1":
        amazon()
    elif ask == "2":
        playstore()
if __name__ == "__main__":
    start()