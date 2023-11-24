from Repositories.BaseRepository import BaseRepository

class ExamRepository(BaseRepository):

    def store(self, data):
        query = ("INSERT INTO exams (name, description, type_exams, exam, result, user_id, schedule_id)"
                 "VALUES (%s, %s, %s, %s, %s, %s, %s)")
        values = (data.get('name'), 
                  data.get('description'), 
                  data.get('type_exams'), 
                  data.get('exam'), 
                  data.get('result'), 
                  data.get('user_id'), 
                  data.get('schedule_id'))

        try:
            self.cursor.execute(query, values)
            self.cnx.commit()
            exam_id = self.cursor.lastrowid
            return {"status": "success", "message": "Exam created successfully", "exam_id": exam_id}
        except Exception as e:
            return {"status": "error", "message": e.msg}

    