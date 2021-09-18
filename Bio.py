import mysql.connector

mydb = mysql.connector.connect(host='localhost',user='root',passwd='',database='python')
mycursor = mydb.cursor()

def AddBio(username):
    firstname = input("Please enter your Firstname: ")
    lastname = input("Please enter your Lastname: ")
    email = in yoput("Please enterur Email: ")

    query = "INSERT INTO userbio VALUES('{}','{}','{}','{}')".format(username,firstname,lastname,email)
    mycursor.execute(query)

    print("Data has been saved successfully!")
AddBio("lakhwan")