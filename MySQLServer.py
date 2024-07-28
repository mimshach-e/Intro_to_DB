# import mysql.connector
# from mysql.connector import Error

# try:
#     mydb = mysql.connector.connect(
#     host = "localhost",
#     user = "root",
#     password = "RichMims@1607"
#     )
#     connection = mydb.cursor()
#     print("Connection to MySQL DB successful")

# except Error as e:
#     print(f"The error '{e}' occured")


# def database():
#     try:
#         connection.execute("CREATE DATABASE IF NOT EXISTS alx_book_store;")
#         mydb.commit()
#         print("Database 'alx_book_store' created successfully!")
        
#     except Error as e:
#         if "database exists" in str(e).lower():
#             print("Database already exists!")
#         else:
#             print(f"The error '{e}' occurred")

# database()    

# connection.close
# mydb.close


import mysql.connector
from mysql.connector import Error

def create_connection():
    try:
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="RichMims@1607"
        )
        print("Connection to MySQL DB successful")
        return mydb
    except Error as e:
        print(f"The error '{e}' occurred")
        return None

def create_database(cursor):
    try:
        cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store;")
        print("Database 'alx_book_store' created successfully!")
    except Error as e:
        if "database exists" in str(e).lower():
            print("Database already exists!")
        else:
            print(f"The error '{e}' occurred")

def main():
    mydb = create_connection()
    if mydb is not None:
        cursor = mydb.cursor()
        create_database(cursor)
        cursor.close()
        mydb.close()

if __name__ == "__main__":
    main()
