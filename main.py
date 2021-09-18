# Importing all the modules..

import sql_loginsys
import gift_card_gen as gf
import spam
import time
import jumble
import passwdGen
#

print("Welcome to LaKhWaN's Code!")

# Functions.

def main():
    while True: 
        choice = ("1. Gift card Generator\n2. Spammer tool\n3. Jumble Game\n4. Friends\n5. Generate Password\nEnter here: ")
        ask = input(choice)
        if ask == "1":
            print('')
            gf.start()
        elif ask == "2":
            print('')
            spam.start()
        elif ask == "3":
            print(''    )
            jumble.start()
        elif ask == "4":
            return
        elif ask == "5":
            passwdGen.passwdGen()
        else:
            print("Invalid Input")
        
# Starting Login/Resgister system.
# sql_loginsys.start()

time.sleep(3)
# Main code:
main()