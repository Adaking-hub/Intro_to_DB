# MySQLServer.py

import mysql.connector
from mysql.connector import Error

try:
    # Connect to MySQL server
    connection = mysql.connector.connect(
        host='localhost',  # Replace with your host
        user='root',       # Replace with your MySQL username
        password=''        # Replace with your MySQL password
    )

    # Create cursor and database
    cursor = connection.cursor()
    cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
    print("Database 'alx_book_store' created successfully!")

except Error as e:
    # Print any connection or execution errors
    print(f"Error while connecting to MySQL: {e}")

finally:
    # Close cursor and connection
    try:
        cursor.close()
    except:
        pass
    try:
        connection.close()
    except:
        pass