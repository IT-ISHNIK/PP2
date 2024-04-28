import psycopg2
from config import load_config

def search_records(pattern):
    """ Search records in the phonebook based on a pattern """
    try:
        config = load_config()
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                cur.execute("""
                    SELECT surname, name,phonenumber FROM PhoneBook
                    WHERE 
                        surname ILIKE %s OR
                        name ILIKE %s OR
                        phonenumber ILIKE %s 
                """, ('%' + pattern + '%', '%' + pattern + '%', '%' + pattern + '%'))
                records = cur.fetchall()
                return records
    except (psycopg2.DatabaseError, Exception) as error:
        print("Error:", error)

if __name__ == '__main__':
    pattern = input("Enter search pattern: ")
    records = search_records(pattern)
    if records:
        print("Search results:")
        for record in records:
            print(record)
    else:
        print("No records found.")