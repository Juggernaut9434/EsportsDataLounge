import psycopg2
from .config import config

class Database():
    conn = None
    cursor = None
    table = "esportsearnings"

    def __init__(self) -> None:
        try:
            self.conn = psycopg2.connect(**config())
            self.cursor = self.conn.cursor()

            self.cursor.execute('SELECT version()')
            db_version = self.cursor.fetchone()
            print(db_version, end="\n\n")

        except(Exception, psycopg2.DatabaseError) as error:
            print(error)
            self.close_connection()

    def __del__(self):
        self.close_connection()

    def close_connection(self):
        if self.conn is not None and not self.conn.closed:
            self.conn.close()
            self.conn = None
            print("Database connection closed.")

    def hello_world(self):
        try:
            if self.conn is None:
                return
            sql = f"SELECT * FROM {self.table} LIMIT 5;"
            self.cursor.execute(sql)
            response = self.cursor.fetchall()

            return response
        except(Exception, psycopg2.DatabaseError) as error:
            print(error)
            self.close_connection()

    def get_genre_data(self):
        try:
            sql = f"SELECT * FROM group_genre;"
            self.cursor.execute(sql)
            return self.cursor.fetchall()
        except(Exception, psycopg2.DatabaseError) as error:
            print(error)
            self.close_connection()

if __name__ == '__main__':
    db = Database()
    db.close_connection()
