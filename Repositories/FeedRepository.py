import mysql.connector
import os

class FeedRepository:

    def __init__(self):

        self.cnx = mysql.connector.connect(
            host=os.getenv("DB_HOST"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD"),
            database=os.getenv("DB_NAME"),
            port=os.getenv("DB_PORT")
        )

        self.cursor = self.cnx.cursor()