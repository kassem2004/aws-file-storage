import os
import psycopg2
from psycopg2 import sql
from db_connection import connect_db

def add_user(username, role):
    conn = connect_db()
    cur = conn.cursor()
    cur.execute("""
                INSERT INTO users (username, role)
                VALUES(%s, %s)""",
                (username, role))
    conn.commit()
    cur.close()
    conn.close()

if __name__ == "__main__":
    username = input("Enter the username you would like to add: ")
    role = input("Enter the role of the user (admin, editer, viewer): ")

    add_user(username=username, role=role)
