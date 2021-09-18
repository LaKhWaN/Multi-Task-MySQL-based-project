# SQL based Login/Register System:

import hashsys
import mysql.connector
import time
import random

# Register:

mydb = mysql.connector.connect(host='localhost',user='root',passwd='',database='mysql')
mycursor = mydb.cursor()

# Random number for hashtag.

numbers = '1234567890'

def register():
    username = input("Please enter your desired username here: ")
    print("You username is: ",username)
    mycursor.execute("Select username from users")
    users = mycursor.fetchall()
    length = len(users)
    for i in range(length):
        if users[i][0] in username:
            print("Username already taken please choose a differnt one.")
            register()
    hashedpassword = hashsys.hashing()

    # MySQL queries:

    user_tuple = [(username, hashedpassword)]
    sql_query="Insert into users values(%s,%s)"
    mycursor.executemany(sql_query,user_tuple)
    mydb.commit()
    time.sleep(1)
    print("You have been registered successfully, please use the same password while logging in next time.")

# Login

def login():
    username = input("Username: ")
    mycursor.execute("Select username from users")
    users = mycursor.fetchall()
    all_users = ""
    for i in range(len(users)):
        all_users+= (users[i][0]+"\n")
    if username not in all_users:
        print("Username not found, please try again.")
        login()
    else:
        pass
    while True:
        password = input("Password: ")
        sql_query = ("SELECT username from users")
        unhashed_password = mycursor.execute(sql_query)
        users = mycursor.fetchall()
        for user_tuple in users:
            for user in user_tuple:
                if user == username:
                    sql_query2 = ("SELECT password from users where username ='{}'".format(username))
                    mycursor.execute(sql_query2)
                    sql_password = mycursor.fetchall()
                    for passwd in sql_password:
                        for sql_passwd in passwd:
                            real_password = sql_passwd
                            unhashed_password = hashsys.unhash(real_password)
        if  unhashed_password == password:
            print("You have logged in successfully!")
            break
        else:
            print("You have entered wrong password please try again!")

# Main Code:
def start():
    print('Login/Register :')
    time.sleep(1)
    ans = input("1. Register\n2. Login\nEnter here: ")
    if ans == '1':
        print("Registeration: ")
        time.sleep(2)
        register()
    elif ans == '2':
        print("Login:")
        time.sleep(2)
        login()
    else:
        print("Invalid Input")
