import sqlite3
#this is gonna be a module that we can use it's functions
#connect the database
conn = sqlite3.connect('Phone.db')
#Create a cursor
cursor = conn.cursor()

def Check_For_Product(Product_Name):
    Products_Name = []
    cursor.execute("SELECT * FROM Details")
    for m in cursor.fetchall():
        Products_Name.append(m[0])
    if Product_Name in Products_Name:
        return 1
    else:
        return 0
def Show_Details(Product_Name):
    cursor.execute("SELECT * FROM Details WHERE Name = '{}'".format(Product_Name))
    Details = cursor.fetchall()[0]
    return Details[0], Details[1], Details[2], Details[3], Details[4], Details[5], Details[6], Details[7], Details[8], Details[9], Details[10]

def Get_Product(Product_Name,Product_RAM, Product_Storage, Product_Camera, Product_SimCard, Product_Battery,Product_Size, Product_Weight, Product_Digikala, Product_Mobile, Product_MeghdadIT,Product_Page):
    Details = []
    Details.append(Product_Name)
    Details.append(Product_RAM)
    Details.append(Product_Storage)
    Details.append(Product_Camera)
    Details.append(Product_SimCard)
    Details.append(Product_Battery)
    Details.append(Product_Size)
    Details.append(Product_Weight)
    Details.append(Product_Digikala)
    Details.append(Product_Mobile)
    Details.append(Product_MeghdadIT)
    Details.append(Product_Page)
    Details.append(1)
    cursor.execute("INSERT INTO Details VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?)" , Details)
    conn.commit()
def Update_Price(Product_Name,Product_Digikala, Product_Mobile, Product_MeghdadIT):
    cursor.execute("UPDATE Details SET Digikala ='{}' WHERE Name = '{}'".format(Product_Digikala, Product_Name))
    cursor.execute("UPDATE Details SET Mobile ='{}' WHERE Name = '{}'".format(Product_Mobile, Product_Name))
    cursor.execute("UPDATE Details SET MeghdadIT ='{}' WHERE Name = '{}'".format(Product_MeghdadIT,Product_Name ))
    conn.commit()

