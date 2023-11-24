import mysql.connector
import os

class BaseRepository:

    def __init__(self):
        self.cursor = self._create_cursor()

    def __del__(self):
        if hasattr(self, 'cursor') and self.cursor:
            self.cursor.close()
        if hasattr(self, 'cnx') and self.cnx.is_connected():
            self.cnx.close()

    def _create_cursor(self):
        self.cnx = mysql.connector.connect(
            host=os.getenv("DB_HOST"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD"),
            database=os.getenv("DB_NAME"),
            port=os.getenv("DB_PORT")
        )

        return self.cnx.cursor()