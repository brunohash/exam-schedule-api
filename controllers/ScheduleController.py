from Handlers.CreateScheduleHandle import CreateScheduleHandle
from Queries.FindAllSchedule import FindAllSchedule

class ScheduleController:
    def store(self, json_data):
        return CreateScheduleHandle().Handle(json_data)
    
    def find(self, json_data):
        return FindAllSchedule().Handler(json_data)
        