import psycopg2
from config import load_config

def create_tables():
    command = """
        CREATE TABLE PhoneBook (
            id SERIAL PRIMARY KEY,
            surname VARCHAR(255) NOT NULL,
            name VARCHAR(255) NOT NULL,
            PhoneNumber VARCHAR(255) 
        )
    """
    try:
        config = load_config()
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                # execute the CREATE TABLE statement
                cur.execute(command)
        print("Table created successfully!")
    except (psycopg2.DatabaseError, Exception) as error:
        print(error)

if __name__ == '__main__':
    create_tables() 
