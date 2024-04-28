import psycopg2
from config import load_config

def update_contact(name, phone_number, new_name, new_phone_number):
    try:
        config = load_config()
        conn = psycopg2.connect(**config)
        cur = conn.cursor()

        # Construct the SQL UPDATE statements
        if new_name:
            update_name_query = """
                UPDATE PhoneBook
                SET name = %s
                WHERE name = %s;
            """
            cur.execute(update_name_query, (new_name, name))

        if new_phone_number:
            update_phone_query = """
                UPDATE PhoneBook
                SET PhoneNumber = %s
                WHERE PhoneNumber = %s;
            """
            cur.execute(update_phone_query, (new_phone_number, phone_number))

        # Check if any rows were updated
        if cur.rowcount == 0:
            print("No matching record found for the provided criteria.")
        else:
            # Commit the transaction
            conn.commit()
            print("Data updated successfully.")
    except (psycopg2.DatabaseError, Exception) as error:
        print(error)
    finally:
        cur.close()
        conn.close()

if __name__ == '__main__':
    name = input("Input name of the contact to update: ")
    phone_number = input("Input phone number of the contact to update: ")
    new_name = input("Input new name (leave empty to skip): ")
    new_phone_number = input("Input new phone number (leave empty to skip): ")

    update_contact(name, phone_number, new_name, new_phone_number)
