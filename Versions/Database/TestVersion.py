import sqlite3

conn = sqlite3.connect('customer.db')

#Create a Cursor
cursor = conn.cursor()

many_customers = [('Wes', 'Brown', 'wes@brown.com'),('Steph', 'Kuewa', 'steph@kuewa.com'),('Dan', 'Pas', 'dan@pas.com')]

#Create a Table

#cursor.executemany("INSERT INTO customers VALUES (?,?,?)", many_customers)
'''
Data Types of sqlite3

NULL
INTEGER
REAL
TEXT
BLOB
'''
#Query the database
cursor.execute('SELECT rowid, * FROM  customers')
for m in cursor.fetchall():
    print(m[1])

#cursor.execute("UPDATE customers SET first_name ='John' WHERE rowid = 1 ")



#commiting our connection
conn.commit()

#close our connection
conn.close()
