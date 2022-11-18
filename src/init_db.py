from configparser import ConfigParser
import psycopg2
import os

def config(filename="database.ini"):
    parser = ConfigParser()
    path = os.path.join('..', filename)
    parser.read(path)

    db = {}
    assert parser.has_section('postgresql'), f"Cannot find postgresql section in prodivded {filename}"
    params = parser.items('postgresql')

    for param in params:
        db[param[0]] = param[1]     # db['host'] = 'localhost'

    return db

def connect_db():
    conn = None
    try:
        conn = psycopg2.connect(**config())
    except(Exception, psycopg2.DatabaseError) as error:
        print(error)

    finally:
        conn.close()
        print("Database connection closed on error.")
