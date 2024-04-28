import psycopg2
from config import load_config

def create_tables():
    commands = [
        """
        CREATE TABLE "user" (
            user_id SERIAL PRIMARY KEY,
            username VARCHAR(255) UNIQUE NOT NULL,
            level INTEGER DEFAULT 1
        )
        """,
        """
        CREATE TABLE user_score (
            score_id SERIAL PRIMARY KEY,
            user_id INTEGER REFERENCES "user" (user_id) ON DELETE CASCADE,
            score INTEGER NOT NULL,
            level INTEGER NOT NULL,
            timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
        """
    ]
    try:
        config = load_config()
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                # execute the CREATE TABLE statements
                for command in commands:
                    cur.execute(command)
        print("Tables created successfully!")
    except (psycopg2.DatabaseError, Exception) as error:
        print(error)

if __name__ == '__main__':
    create_tables()
