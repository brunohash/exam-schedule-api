from Repositories.ExamsRepository import ExamRepository

class ExamsHandle:
    def Handle(self, data):
        
        required_fields = ['name', 'description', 'type_exams', 'exam', 'result', 'user_id', 'schedule_id']

        if any(data.get(field) == '' for field in required_fields):
            return {"status": "error", "code": 400, "message": "All fields are required"}
        
        else:

            print(data)
            insert = ExamRepository().store(data)

            if insert.get('status') == 'success':
                return {"status": "success", "code": 201, "message": "Register successful"}
            else:
                return {"status": "error", "code": 400, "message": insert.get('message')}

