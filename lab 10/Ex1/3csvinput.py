import psycopg2
from config import load_config

def import_data_from_csv():
    """Import data into the PhoneBook table from a CSV file"""
    command = """
    COPY PhoneBook(surname,name,phonenumber)
    FROM 'C:\Data.csv'
    DELIMITER ';'
    CSV HEADER;
    """
    try:
        config = load_config()
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                # Execute the COPY command to import data from CSV
                cur.execute(command)
        print("Data imported successfully!")
    except (psycopg2.DatabaseError, Exception) as error:
        print(error)

if __name__ == '__main__':
    import_data_from_csv()
