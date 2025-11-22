import mysql.connector
from dotenv import load_dotenv
import os

load_dotenv()

MYSQL_HOST = os.getenv("MYSQL_HOST")
MYSQL_USER = os.getenv("MYSQL_USER")
MYSQL_PASSWORD = os.getenv("MYSQL_PASSWORD")
MYSQL_DB = os.getenv("MYSQL_DB")

def connect():
    return mysql.connector.connect(
        host=MYSQL_HOST,
        user=MYSQL_USER,
        password=MYSQL_PASSWORD,
        database=MYSQL_DB
    )

def create_metadata(game):
    conn = connect()
    cursor = conn.cursor()

    data_dict = (game)
    placeholders = ', '.join(['%s'] * len(data_dict))
    columns = ', '.join(data_dict.keys())
    query = "INSERT INTO test_customer (%s) VALUES (%s)" % (columns, placeholders)
    
    cursor.execute(query, list(data_dict.values()))
    conn.commit()
    conn.close()
    return cursor.lastrowid