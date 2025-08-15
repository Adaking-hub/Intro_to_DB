# MySQLServer.py

import mysql.connector

try:
    # Connect to MySQL server
    connection = mysql.connector.connect(
        host='localhost',  # Replace with your MySQL host
        user='root',       # Replace with your MySQL username
        password=''        # Replace with your MySQL password
    )

    # Create cursor and database
    cursor = connection.cursor()
    cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
    print("Database 'alx_book_store' created successfully!")

except mysql.connector.Error as e:
    # Handle MySQL connection or execution errors
    print(f"Error while connecting to MySQL: {e}")

finally:
    # Close cursor and connection safely
    try:
        cursor.close()
    except:
        pass
    try:
        connection.close()
    except:
        pass
