import hashlib

from Repositories.BaseRepository import BaseRepository
class AuthenticationRepository(BaseRepository):

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
            
            if type_user == 1:
                type_id = data.get("type")
            elif type_user == 2 or type_user == 3:
                type_id = 3

            print("Type User:", type_user, "\n", "Type Id:", type_id)

            # Criptografar a senha usando MD5
            hashed_password = hashlib.md5(password.encode()).hexdigest()

            query = ("INSERT INTO users (name, email, age, birthdate, street, city, state, zip, phone, password, type_id)"
                    "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)")

            values = (name, email, age, birthdate, address['street'], address['city'], address['state'], address['zip'], phone, hashed_password, type_id)

            self.cursor.execute(query, values)
        
            self.cnx.commit()
            self.cursor.close()

            if self.cursor.rowcount > 0:
                return {"status": "success", "message": "Register successful"}
            else:
                return {"status": "error", "message": "Register failed"}
            
        except Exception as e:
            return {"status": "error", "message": str(e)}
