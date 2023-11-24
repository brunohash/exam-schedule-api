from Repositories.BaseRepository import BaseRepository
from datetime import date, time, timedelta
import json

class FindAllSchedule(BaseRepository):
    def find(self, id):
        try:
            query = "SELECT schedules.id, schedules.date, schedules.time, schedules.status, \
                users.name AS user_name, users.email AS user_email, \
                type_exams.name AS type_exam_name, type_exams.description AS type_exam_description \
                FROM schedules \
                INNER JOIN users ON schedules.user_id = users.id \
                INNER JOIN type_exams ON schedules.type_exams = type_exams.id \
                WHERE schedules.id = %s"

            values = (id,)

            self.cursor.execute(query, values)
            result = self.cursor.fetchone()

            if result:
                columns = [desc[0] for desc in self.cursor.description]

                # formatted_result = {col: self.serialize_value(result[i]) for i, col in enumerate(columns)}
                formatted_result = {col: result[i] for i, col in enumerate(columns)}

                print(formatted_result)

                #serialize date and time to isoformat timedelta
                formatted_result['date'] = self.serialize_value(formatted_result['date'])
                formatted_result['time'] = self.serialize_value(formatted_result['time'])

                # formatted_result['time'] = self.serialize_value(formatted_result['time'])
                # formatted_result['time'] = formatted_result['time'].isoformat()

                return {"status": "success", "code": 200, "data": json.loads(json.dumps(formatted_result))}
            else:
                return {"status": "error", "code": 404, "message": "Schedule not found"}
        except Exception as e:
            return {"status": "error", "code": 500, "message": str(e)}

    def serialize_value(self, value):
        if isinstance(value, date) or isinstance(value, time):
            return value.isoformat()
        
        if isinstance(value, timedelta):
            return str(value)
        return value