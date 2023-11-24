from Repositories.ScheduleRepository import ScheduleRepository

class FindAllSchedule:
    def Handler(self, id):
        return ScheduleRepository.ScheduleRepository().find(id) 
