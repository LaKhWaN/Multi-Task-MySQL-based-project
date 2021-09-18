# Importing My-SQL module.

import mysql.connector

# Details of the hoster.
host_name = 'freedb.tech'
username = 'freedb_upender'
password = 'upender9'
db = 'freedb_python'

# Some starters.

mydb = mysql.connector.connect(host=host_name,user=username,passwd=password,database=db)
mycursor = mydb.cursor()

def chat():
    while True:
        try:
            sql_query = 'Create table ' + name + '(message varchar(200))'
            mycursor.execute(sql_query)
        except Exception:
            print(name,end=': ')
            message = input()
            sql_query = 'Insert into '+name+' values('+'"'+message+'")'
            mycursor.execute(sql_query)
            mydb.commit()
            #ask = input("Would you like to check for message? (y/n) [Press 'y' because its in alpha stages or program will crash]: ")
            #if ask == 'y' or "Y":
            readchat()


def readchat():
    mycursor.execute("Select message from "+name_2)
    data = mycursor.fetchall()
    for i in data:
        print(i)
    mycursor.execute("DELETE FROM "+ name_2)
    chat()

name = input("Please enter your name here: ")
name_2 = input("Please enter name of your friend: ")

ask1 = input("1. Send Message\n2. Read message\nEnter here: ")
if ask1 == "1":
    chat()
elif ask1 == "2":
    readchat()
else:
    print("Invalid Input")
