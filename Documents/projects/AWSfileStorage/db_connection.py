import psycopg2
from psycopg2 import sql
import os

def connect_db():
    conn = psycopg2.connect(database = os.getenv("DB_NAME"),
                            user=os.getenv("DB_USER"),
                            host=os.getenv("DB_HOST"),
                            password=os.getenv("DB_PASSWORD"),
                            port=os.getenv("DB_PORT")
                            )
    return conn

def create_users_table(conn):
    cur = conn.cursor()
    cur.execute("""CREATE TABLE IF NOT EXISTS users (
    user_id SERIAL PRIMARY KEY,
    username VARCHAR(50) NOT NULL UNIQUE,
    role VARCHAR(20) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP);
                """)
    
    conn.commit()

    cur.close()

if __name__ == "__main__":
    connection = connect_db()
    
    create_users_table(connection)
    
    connection.close()
    