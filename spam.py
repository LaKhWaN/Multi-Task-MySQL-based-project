import time
import pyautogui


# Functions :

# Spamming tool:

def start():
    print('Spamming Tool: ')
    #time.sleep(3)
    file = open("test.txt", "w")
    while True:
        words = input("Please enter the words one by one which you would like to spam:\n")
        file.write(words + "\n")
        ask2 = input("Would you like to enter more?(Y/N):\n")
        if ask2 == "N":
            break
    file.close()
    print("All data has been saved!")
    #time.sleep(2)
    num = int(input("How many times would you like to spam the victim?(Enter number like 100,20,35):\n"))
    print("Make sure to open the chat box and click cursor in it else it will not work.")
    time.sleep(2)
    input("Press enter to start the spamming tool.")
    for i in range(5, 0, -1):
        print("Time left for starting the spam->", i)
        time.sleep(1)
    for ch in range(num):
        file = open("test.txt", "r")
        for word in file:
            pyautogui.typewrite(word)
            pyautogui.press("enter")
        file.close()
    time.sleep(2)
    input("Thanks for using the code :D")
