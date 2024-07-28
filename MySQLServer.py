import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "RichMims@1607"
)
connection = mydb.cursor()

def database():
    if True:
        connection.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
        mydb.commit()
        print("Database 'alx_book_store' created successfully!")
    
    print("Database already exists!")

database()    

connection.close
mydb.close
