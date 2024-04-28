import psycopg2
from config import load_config

def delete_contact(name, phone_number):
    try:
        config = load_config()
        conn = psycopg2.connect(**config)
        cur = conn.cursor()

        # Construct the SQL DELETE statements
        if name:
            delete_name = """
                DELETE FROM PhoneBook WHERE name = %s;
            """
            cur.execute(delete_name, (name,))  # Pass the parameter as a tuple

        if phone_number:
            delete_phone_number = """
                DELETE FROM PhoneBook WHERE phonenumber = %s;
            """
            cur.execute(delete_phone_number, (phone_number,))  # Pass the parameter as a tuple

        # Check if any rows were deleted
        if cur.rowcount == 0:
            print("No matching record found for the provided criteria.")
        else:
            # Commit the transaction
            conn.commit()
            print("Data deleted successfully.")
    except (psycopg2.DatabaseError, Exception) as error:
        print(error)
    finally:
        cur.close()
        conn.close()

if __name__ == '__main__':
    name = input("Input name of the contact to delete (leave empty to skip): ")
    phone_number = input("Input phone number of the contact to delete (leave empty to skip): ")

    delete_contact(name, phone_number)
