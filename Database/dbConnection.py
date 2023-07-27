import mysql.connector
import logging
import os
from dotenv import find_dotenv, load_dotenv
load_dotenv(find_dotenv())

# Connect to the MySQL database
cnx = mysql.connector.connect(
    host=os.getenv('HOST'),    # Replace with your MySQL server host
    user=os.getenv('USER'),     # Replace with your MySQL username
    password=os.getenv('PASSWORD'), # Replace with your MySQL password
    database=os.getenv('DATABASE')  # Replace with your MySQL database name
)

# Set up logging
logging.basicConfig(filename='./Logs/requests.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Function to insert data into the database
def insert_data(symbol, name, last_price, change_value, percentage_change):
    try:
        cursor = cnx.cursor()

        # Check if the record already exists
        sql = "SELECT * FROM stocks WHERE Symbol = %s"
        cursor.execute(sql, (symbol,))
        existing_record = cursor.fetchone()

        if existing_record:
            # If the record exists, update it
            sql = "UPDATE stocks SET Name = %s, Last_Price = %s, Change_Value = %s, Percentage_Change = %s WHERE Symbol = %s"
            cursor.execute(sql, (name, last_price, change_value, percentage_change, symbol))
        else:
            # If the record does not exist, insert a new record
            sql = "INSERT INTO stocks (Symbol, Name, Last_Price, Change_Value, Percentage_Change) VALUES (%s, %s, %s, %s, %s)"
            cursor.execute(sql, (symbol, name, last_price, change_value, percentage_change))

        # Commit changes to the database
        cnx.commit()
        logging.info("Data inserted or updated successfully.")
    except Exception as e:
        logging.error(f"Error: {e}")
        cnx.rollback()
    finally:
        cursor.close()
    return

def getData():
    try:
        cursor = cnx.cursor(dictionary=True)

        # Fetch all data from the "Stocks" table
        sql = "SELECT * FROM stocks"
        cursor.execute(sql)
        data = cursor.fetchall()

        # Close the cursor and connection
        cursor.close()

        return data
    except Exception as e:
        logging.error(f"Error: {e}")
        cnx.rollback()
        cnx.close()
        return None