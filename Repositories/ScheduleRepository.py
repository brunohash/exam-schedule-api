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
            
    def find(self, id):
        query = "SELECT schedules.id, schedules.date, schedules.time, schedules.status, \
        users.name, users.email, exams.name, type_exams.name, type_exams.description \
        FROM schedules \
        INNER JOIN users ON schedules.user_id = users.id \
        INNER JOIN exams ON schedules.exam_id = exams.id \
        INNER JOIN type_exams ON schedules.exam_id = type_exams.id \
        WHERE schedules.id = %s"

        values = (id,)
        
        result = self.execute(query, values)

        self.cnx.commit()
        self.cursor.close()
        
        if result:
            return {"status": "success", "code": 200, "data": result}
        else:
            return {"status": "error", "code": 404, "message": "Schedule not found"}

        