import mysql.connector
from mysql.connector import errorcode

def create_database():
    """
    Connects to MySQL server and creates the alx_book_store database.
    """
    try:
        # Establish connection to the MySQL server
        # Replace 'your_password' with the actual password for the 'root' user
        cnx = mysql.connector.connect(
            host="localhost",
            user="root",
            password="7456", 
        )
        cursor = cnx.cursor()
        
        # SQL command to create the database if it doesn't exist
        # Using "IF NOT EXISTS" prevents an error if the database is already there
        cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
        
        print("Database 'alx_book_store' created successfully!")

    except mysql.connector.Error as err:
        # Handle specific connection errors
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your user name or password")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
        else:
            print(f"Failed to create database: {err}")
    finally:
        # Ensure the connection is closed
        if 'cursor' in locals() and cursor:
            cursor.close()
        if 'cnx' in locals() and cnx.is_connected():
            cnx.close()

if __name__ == "__main__":
    create_database()