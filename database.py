import mysql.connector
from config import DB_config

def get_connection():
    try:
        connection=mysql.connector.connect(**DB_config)
        
        if connection.is_connected():
            print("Database connected successfully")
            
        return connection

    except mysql.connector.Error as err:
        print("Database not connected:",err)
        return None
        