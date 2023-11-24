import mysql.connector
import os

class UserRepository:
    def __init__(self):

        self.cnx = mysql.connector.connect(
            host=os.getenv("DB_HOST"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD"),
            database=os.getenv("DB_NAME"),
            port=os.getenv("DB_PORT")
        )

        self.cursor = self.cnx.cursor()

    def find(self, user_id):
        query = "SELECT * FROM users WHERE id = %s"
        values = (user_id,)

        self.cursor.execute(query, values)
        result = self.cursor.fetchone()

        return result

    def all(self):
        query = "SELECT * FROM users"
        self.cursor.execute(query)
        result = self.cursor.fetchall()

        return result
    
    