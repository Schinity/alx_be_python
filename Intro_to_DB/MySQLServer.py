import mysql.connector
from mysql.connector import Error

try:
    # Open connection to MySQL server (no database specified yet)
    connection = mysql.connector.connect(
        host='localhost',
        user='alx',
        password='#!BigT33'
    )

    if connection.is_connected():
        cursor = connection.cursor()
        # Create database if it doesn't exist
        cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
        print("Database 'alx_book_store' created successfully!")

except Error as e:
    print(f"Error: {e}")

finally:
    # Close cursor and connection safely
    if 'cursor' in locals() and cursor:
        cursor.close()
    if 'connection' in locals() and connection.is_connected():
        connection.close()
        print("MySQL connection closed.")
