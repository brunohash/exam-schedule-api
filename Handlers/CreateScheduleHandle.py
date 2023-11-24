import Repositories.ScheduleRepository as ScheduleRepository

class CreateScheduleHandle:
    def Handle(self, data):
        
        required_fields = ['date', 'time', 'user_id', 'type_exams']

        if any(data.get(field) == '' for field in required_fields):
            return {"status": "error", "code": 400, "message": "All fields are required"}
        
        else:

            print(data)
            insert = ScheduleRepository.ScheduleRepository().store(data)

            if insert.get('status') == 'success':
                return {"status": "success", "code": 201, "message": "Register successful"}
            else:
                return {"status": "error", "code": 400, "message": insert.get('message')}

