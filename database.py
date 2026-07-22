import mysql.connector
from mysql.connector import Error
from config import DB_config


def get_connection():
   

    try:
        connection = mysql.connector.connect(**DB_config)

        if connection.is_connected():
            return connection

    except Error as error:
        print(f"Database Error: {error}")

    return None


def execute_query(query, values=None):
   

    connection = get_connection()

    if connection is None:
        return False

    cursor = connection.cursor()

    try:

        if values:
            cursor.execute(query, values)
        else:
            cursor.execute(query)

        connection.commit()
        return True

    except Error as error:
        print(f"Query Error: {error}")
        return False

    finally:
        cursor.close()
        connection.close()


def fetch_all(query, values=None):
    

    connection = get_connection()

    if connection is None:
        return []

    cursor = connection.cursor()

    try:

        if values:
            cursor.execute(query, values)
        else:
            cursor.execute(query)

        return cursor.fetchall()

    except Error as error:
        print(f"Query Error: {error}")
        return []

    finally:
        cursor.close()
        connection.close()


def fetch_one(query, values=None):
    

    connection = get_connection()

    if connection is None:
        return None

    cursor = connection.cursor()

    try:

        if values:
            cursor.execute(query, values)
        else:
            cursor.execute(query)

        return cursor.fetchone()

    except Error as error:
        print(f"Query Error: {error}")
        return None

    finally:
        cursor.close()
        connection.close()