from database import get_connection

def main():
    connection = get_connection()
    
    if connection:
        print("Welcome to Secure Bank")
        connection.close()
        print("Connection closed")
        
if __name__== "__main__":
    main()