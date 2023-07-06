import sqlite3
#this is gonna be a module that we can use it's functions

#Connect to database
conn = sqlite3.connect('Users.db')
#Create A Cursor
cursor = conn.cursor()


#Define a function that add users to the database and return id of the user to the app as current user for showing in profile page
def Register(username, email, password):
    Usernames_list = []
    Emails_List = []
    User = [username,email,password]
    cursor.execute("SELECT rowid, * FROM Users ")
    for m in cursor.fetchall():
        Usernames_list.append(m[1])
        Emails_List.append(m[2])
    if username not in Usernames_list and email not in Emails_List:
        cursor.execute("INSERT INTO Users VALUES (? , ? , ?)" , User)
        cursor.execute("SELECT rowid, * FROM Users WHERE Name = '{}'".format(username) )
        id = cursor.fetchall()[0][0]
        conn.commit()
        return 1, id
    else:
        return 0 , "User Joined Before!!"


#Define a function that show users info in profile page that returns name and email of the user
def Show_User_Info(id):
    cursor.execute('SELECT rowid, * FROM Users WHERE rowid = "{}"'.format(id))
    Name = cursor.fetchall()[0][1]
    print(Name)
    cursor.execute('SELECT rowid, * FROM Users WHERE rowid = "{}"'.format(id))
    Email = cursor.fetchall()[0][2]
    print(Email)
    conn.commit()
    return Name, Email

#Define a function that change passwords by their id 
def Change_Password(id, old_password, new_password):
    cursor.execute('SELECT rowid, * FROM Users WHERE rowid = "{}"'.format(id))
    Password = cursor.fetchall()[0][3]
    if old_password == Password:
        cursor.execute('UPDATE Users SET password = "{}" WHERE rowid = "{}"'.format(new_password, id))
        return 1
    else:
        return 0
    conn.commit()

#Define a fucntion that login by name or email and password
def Login(name, password):
    Usernames_list = []
    Emails_List = []
    User = [name,password]
    cursor.execute("SELECT rowid, * FROM Users ")
    for m in cursor.fetchall():
        Usernames_list.append(m[1])
        Emails_List.append(m[2])
    if name in Emails_List:
        cursor.execute('SELECT rowid, * FROM Users WHERE Email = "{}"'.format(name))
        id = cursor.fetchall()[0][0]
        cursor.execute('SELECT rowid, * FROM Users WHERE Email = "{}"'.format(name))
        Pass = cursor.fetchall()[0][3]
        if Pass == password:
            return 1, id
        else:
            return 0, 'Password Not Correct!'
    elif name in Usernames_list:
        cursor.execute('SELECT rowid, * FROM Users WHERE Name = "{}"'.format(name))
        id = cursor.fetchall()[0][0]
        cursor.execute('SELECT rowid, * FROM Users WHERE Name = "{}"'.format(name))
        Pass = cursor.fetchall()[0][3]
        if Pass == password:
            return 1, id
        else:
            return 0, 'Password Not Correct!'
    else:
        return 0, 'You Should Join First!!'




