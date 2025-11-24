from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
import os

load_dotenv()


MYSQL_HOST = os.getenv("MYSQL_HOST")
MYSQL_PORT = os.getenv("MYSQL_PORT")
MYSQL_USER = os.getenv("MYSQL_USER")
MYSQL_PASSWORD = os.getenv("MYSQL_PASSWORD")
MYSQL_DB = os.getenv("MYSQL_DB")

def connect():
    return create_engine(
        url="mysql://{0}:{1}@{2}:{3}/{4}".format(MYSQL_USER, MYSQL_PASSWORD, MYSQL_HOST, MYSQL_PORT, MYSQL_DB)
    )

engine = connect()
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

"""

def connect():
    return mysql.connector.connect(
        host=MYSQL_HOST,
        port=MYSQL_PORT,
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
    query = "INSERT IGNORE INTO test_customer (%s) VALUES (%s)" % (columns, placeholders)

    cursor.execute(query, list(data_dict.values()))
    conn.commit()
    conn.close()
    return cursor.fetchall()

def flush_duplicates():
    conn = connect()
    cursor = conn.cursor()
    query = "CREATE TABLE mytable_temp AS SELECT DISTINCT * FROM test_customer; DROP TABLE test_customer; RENAME TABLE mytable_temp TO test_customer"
    query = filter(None, query.split(';'))
    for i in query:
        cursor.execute(i.strip() + ';')
  
    #cursor.execute(query)
    conn.commit()
    conn.close()

def delete_dupe(game):
    gameID = game["GameID"]

    #switch to sqlalchemy

"""