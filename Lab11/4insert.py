import psycopg2
from config import load_config

def get_contacts_by_name(surname, limit, offset):
    try:
        config = load_config()
        conn = psycopg2.connect(**config)
        cur = conn.cursor()

        query = "SELECT * FROM PhoneBook WHERE surname = %s LIMIT %s OFFSET %s"
        cur.execute(query, (surname, limit, offset))
        
        contacts = cur.fetchall()
        
        return contacts
    except (psycopg2.DatabaseError, Exception) as error:
        print("Error fetching data by surname:", error)
        return None
    finally:
        if cur:
            cur.close()
        if conn:
            conn.close()

def get_contacts_by_phone(phone_number, limit, offset):
    try:
        config = load_config()
        conn = psycopg2.connect(**config)
        cur = conn.cursor()

        query = "SELECT * FROM PhoneBook WHERE phonenumber = %s LIMIT %s OFFSET %s"
        cur.execute(query, (phone_number, limit, offset))
        
        contacts = cur.fetchall()
        
        return contacts
    except (psycopg2.DatabaseError, Exception) as error:
        print("Error fetching data by phone number:", error)
        return None
    finally:
        if cur:
            cur.close()
        if conn:
            conn.close()
            
surname_found = input("Enter surname that you need: ")
phone_number_found = input("Enter phonenumber that you need: ")
limit = int(input("Enter limit: "))
offset = int(input("Enter offset: "))

if __name__ == '__main__':
    # Example usage: get contacts with a specific surname
    contacts_with_surname = get_contacts_by_name(surname_found, limit, offset)
    if contacts_with_surname:
        print(f"Contacts with surname {surname_found}:", contacts_with_surname)
    else:
        print(f"No contacts found with surname {surname_found}.")

    # Example usage: get contacts with a specific phone number
    contacts_with_phone = get_contacts_by_phone(phone_number_found, limit, offset)
    if contacts_with_phone:
        print(f"Contacts with phone number {phone_number_found} :", contacts_with_phone)
    else:
        print(f"No contacts found with phone number {phone_number_found}.")
