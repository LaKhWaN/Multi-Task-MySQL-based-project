import mysql.connector

mydb = mysql.connector.connect(host='localhost',user='root',passwd='',database='python')
mycursor = mydb.cursor()

def addfriend(username):
        friendname = input('Enter the username of your friend: ')
        mycursor.execute("Select username from users")
        users = mycursor.fetchall()
        length = len(users)
        allusers = []
        mycursor.execute('Select friendname from friend')
        friends = mycursor.fetchall()
        length1 = len(users)
        friendlist = []
        for i in range(length1):
                friendlist.append(friends[i][0])
        for i in range(length):
                allusers.append(users[i][0])
        if friendname in friendlist:
                print('Friend already added.')
        elif friendname not in allusers:
                print("No user found!")
                addfriend(username)
        else:
                mycursor.execute("Select username from users")
                users = mycursor.fetchall()
                for user in users:
                        for i in user:
                                if i == friendname:
                                        query = "Insert into friend values('{}','{}')".format(username,friendname)
                                        mycursor.execute(query)
                                        mydb.commit()
                                        print('Friend added successfully!')

