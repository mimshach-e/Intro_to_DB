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

# connection.close()
# mydb.close()


import mysql.connector
from mysql.connector import Error

try:
    # Establish connection to the MySQL server
    mydb = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "RichMims@1607"
    )
    connection = mydb.cursor()
    print("Connection to MySQL DB successful")

    def create_database():
        try:
            # Execute SQL command to create the database
            connection.execute("CREATE DATABASE IF NOT EXISTS alx_book_store;")
            mydb.commit()
            print("Database 'alx_book_store' created successfully!")
        except mysql.connector.Error as e:
            if "database exists" in str(e).lower():
                print("Database already exists!")
            else:
                print(f"The error '{e}' occurred")

    # Call the function to create the database
    create_database()

except mysql.connector.Error as e:
    print(f"The error '{e}' occurred")

finally:
    # Close the cursor and connection
    if connection:
        connection.close()
    if mydb.is_connected():
        mydb.close()
        print("MySQL connection is closed")
