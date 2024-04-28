import psycopg2
from config import load_config

def update_contact(username=None, phone_number=None):
    try:
        config = load_config()
        conn = psycopg2.connect(**config)
        cur = conn.cursor()

        # Construct the SQL SELECT query to check if the contact exists
        select_query = """
            SELECT * FROM PhoneBook WHERE"""
        
        # Check if name or phone number is provided
        if username:
            select_query += " name = %s"
            search_value = username
        elif phone_number:
            select_query += " phonenumber = %s"
            search_value = phone_number
        else:
            print("Please provide a name or phone number.")
            return
        
        select_query += ";"
        cur.execute(select_query, (search_value,))

        # Fetch all the results
        existing_contacts = cur.fetchall()

        if not existing_contacts:
            print("No matching record found for the provided criteria.")
            return
        else:
            print("Matching records found for the provided criteria:")
            for contact in existing_contacts:
                print("Contact Information:")
                print("Name:", contact[2])  # Assuming name is the second column (index 1)
                print("Phone Number:", contact[3])  # Assuming phone number is the third column (index 2)
                print("--------------------")

    except (psycopg2.DatabaseError, Exception) as error:
        print(error)
    finally:
        cur.close()
        conn.close()

if __name__ == '__main__':
    name = input("Input name of the contact to check (leave empty to skip): ")
    phone_number = input("Input phone number of the contact to check (leave empty to skip): ")

    update_contact(username=name, phone_number=phone_number)
