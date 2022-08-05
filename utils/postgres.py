import psycopg2
from core.secrets import PSQL_HOST, PSQL_PORT, PSQL_USER, PSQL_PSWD


class Connection:
    def __init__(self, host=PSQL_HOST, port=PSQL_PORT, user=PSQL_USER, password=PSQL_PSWD, db=None):
        self.connection = psycopg2.connect(host=host, port=port, user=user, password=password, database=db)
        self.cursor = self.connection.cursor()

    def fetch_all(self, query):
        try:
            with self.connection:
                with self.cursor as cursor:
                    cursor.execute(query)
                    data = cursor.fetchall()
                    return data

        finally:
            if self.connection:
                self.connection.close()

    def fetch_one(self, query):
        try:
            with self.connection:
                with self.cursor as cursor:
                    cursor.execute(query)
                    data = cursor.fetchone()
                    return data

        finally:
            if self.connection:
                self.connection.close()
