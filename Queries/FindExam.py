
from Repositories.BaseRepository import BaseRepository

class FindExam(BaseRepository):
    def find(self, exam_id):
        query = "SELECT * FROM exams WHERE id = %s"
        values = (exam_id,)

        self.cursor.execute(query, values)
        result = self.cursor.fetchone()

        if result:
            columns = ["id", "name", "description", "type_exams", "exam", "result", "user_id", "schedule_id"]
            formatted_result = {col: result[i] for i, col in enumerate(columns)}
            return {"status": "success", "code": 200, "data": formatted_result}
        else:
            return {"status": "error", "code": 404, "message": "Exam not found"}
    
    def findTypeExam(self):
        query = "SELECT * FROM type_exams"

        self.cursor.execute(query)
        result = self.cursor.fetchall()

        if result:
            columns = ["id", "name", "description"]
            formatted_result = [{col: result[i] for i, col in enumerate(columns)} for result in result]
            return {"status": "success", "code": 200, "data": formatted_result}
        else:
            return {"status": "error", "code": 404, "message": "Exam not found"}
        
    def close_connection(self):
        self.cursor.close()
        self.cnx.close()
