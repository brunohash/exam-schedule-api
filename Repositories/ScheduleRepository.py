from Repositories.BaseRepository import BaseRepository
class ScheduleRepository(BaseRepository):

    def store(self, data):
        try:
            query = "INSERT INTO schedules (date, time, status, user_id, type_exams) VALUES (%s, %s, %s, %s, %s)"
            values = (data.get('date'), data.get('time'), "PENDENTE", data.get('user_id'), data.get('type_exams'))
            result = self.cursor.execute(query, values)

            self.cnx.commit()
            self.cursor.close()

            if(self.cursor.rowcount > 0):
                return {"status": "success", "code": 201, "message": "Register successful"}
            else:
                return {"status": "error", "code": 400, "message": "Register failed"}
            
        except Exception as e:
            return {"status": "error", "code": 400, "message": str(e)}
            
    
        