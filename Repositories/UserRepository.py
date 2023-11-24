from Repositories.BaseRepository import BaseRepository
class UserRepository(BaseRepository):

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
    
    