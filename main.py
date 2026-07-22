from database import (
    get_connection,
    fetch_all
)


def main():

    print("=" * 45)
    print("        SecureBank Management System")
    print("=" * 45)

    connection = get_connection()

    if connection:

        print("Database Connected Successfully!\n")

        connection.close()

        tables = fetch_all("SHOW TABLES")

        print("Available Tables:\n")

        for table in tables:
            print(f"- {table[0]}")

    else:

        print("Unable to connect to database.")


if __name__ == "__main__":
    main()