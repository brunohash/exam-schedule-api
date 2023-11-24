import mysql.connector
import os
import hashlib

class AuthenticationRepository:

    def __init__(self):

        self.cnx = mysql.connector.connect(
            host=os.getenv("DB_HOST"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD"),
            database=os.getenv("DB_NAME"),
            port=os.getenv("DB_PORT")
        )

        self.cursor = self.cnx.cursor()

    def auth(self, email, input_password):
        query = "SELECT id, name, email, type_id, password FROM users WHERE email = %s"
        values = (email,)

        self.cursor.execute(query, values)
        result = self.cursor.fetchone()

        print(result)
        
        if result:
            id, name, email, type_id, stored_password = result

            input_password_hash = hashlib.md5(input_password.encode()).hexdigest()

            if input_password_hash == stored_password:
                columns = ["id", "name", "email", "type_id", "password"]
                formatted_result = {col: result[i] for i, col in enumerate(columns)}
                return formatted_result
            else:
                return False
        else:
            return False
        
    def store(self, data):

        try:
            name = data.get("name", "")
            email = data.get("email", "")
            age = data.get("age", "")
            birthdate = data.get("birthdate", "")
            address = data.get("address", {"street": "", "city": "", "state": "", "zip": ""})
            phone = data.get("phone", "")
            password = data.get("password", "")

            type_user = data.get("type_user")
            type_id = data.get("type")

            if type_user == 3:
                return {"status": "error", "message": "Você não tem permissão para realizar esta ação"}
            else:
                type_id = data.get("type_id", 3)

            # Criptografar a senha usando MD5
            hashed_password = hashlib.md5(password.encode()).hexdigest()

            query = ("INSERT INTO users (name, email, age, birthdate, street, city, state, zip, phone, password, type_id)"
                    "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)")

            values = (name, email, age, birthdate, address['street'], address['city'], address['state'], address['zip'], phone, hashed_password, type_id)

            self.cursor.execute(query, values)
        
            self.cnx.commit()
            self.cursor.close()

            if self.cursor.rowcount:
                return {"status": "success", "message": "Register successful"}
            else:
                return {"status": "error", "message": "Register failed"}
            
        except mysql.connector.Error as err:
            return {"status": "error", "message": err.msg}
