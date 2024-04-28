import psycopg2
from config import load_config

def insert_from_console():
    try:
        config = load_config()
        conn = psycopg2.connect(**config)
        cur = conn.cursor()

        surname = input("Enter Last Name: ")
        name = input("Enter First Name: ")
        phonenumber = input("Enter Phone Number: ")

        cur.execute("""
            INSERT INTO PhoneBook (surname, name, phonenumber)
            VALUES (%s, %s, %s )
        """, (surname, name, phonenumber))

        conn.commit()
        print("Data inserted successfully from console.")
    except (psycopg2.DatabaseError, Exception) as error:
        print(error)
    finally:
        cur.close()
        conn.close()

if __name__ == '__main__':
    insert_from_console()