import sqlite3
#this is gonna be a module that we can use it's functions

#Connect to database
conn = sqlite3.connect('Users.db')
#Create A Cursor
cursor = conn.cursor()

#Create A Table
cursor.execute("""CREATE TABLE  Users (
            Name TEXT,
            Email TEXT,
            Password TEXT
    )""") 


#Define a function that add users to the database and return id of the user to the app as current user for showing in profile page
def Register(username, email, password):
    cursor.execute("SELECT rowid, * FROM Users ")
    Usernames_list = cursor.fetchall()[1]
    Emails_List = cursor.fetchall()[2]
    if username not in Usernames_list and email not in Emails_List:
        cursor.execute("""INSERT INTO Users (username, email, password)
        """)
        cursor.execute('SELECT rowid, * FROM Users WHERE Name = username AND Email = email')
        id = cursor.fetchone()[0][0]
        conn.commit()
        return 1, id
    else:
        return 0 , "User Joined Before!!"


#Define a function that show users info in profile page that returns name and email of the user
def Show_User_Info(id):
    cursor.execute('SELECT rowid, * FROM Users WHERE rowid = id')
    Name = cursor.fetchone()[0][1]
    Email = cursor.fetchone()[0][2]
    conn.commit()
    return Name, Email

#Define a function that change passwords by their id 
def Change_Password(id, old_password, new_password):
    cursor.execute('SELECT rowid, * FROM Users WHERE rowid =id')
    Password = cursor.fetchone()[0][3]
    if old_password == Password:
        cursor.execute('UPDATE Users SET password = new_password WHERE rowid = old_password')
    conn.commit()
def Login(name, password):
    cursor.execute("SELECT rowid, * FROM Users ")
    Usernames_list = cursor.fetchall()[1]
    Emails_List = cursor.fetchall()[2]
    if name in Emails_List:
        cursor.execute('SELECT rowid, * FROM Users WHERE Email = name')
        id = cursor.fetchone()[0][0]
        Pass = cursor.fetchone()[0][3]
        if Pass == password:
            return 1, id
    elif name in Usernames_list:
        cursor.execute('SELECT rowid, * FROM Users WHERE Email = name')
        id = cursor.fetchone()[0][0]
        Pass = cursor.fetchone()[0][3]
        if Pass == password:
            return 1, id
    else:
        return 0, 'You Should First Join!!'




