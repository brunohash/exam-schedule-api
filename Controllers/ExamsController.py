from Handlers.ExamsHandle import ExamsHandle
from Queries.FindExam import FindExam

class ExamsController:
    def store(self, json_data):
        return ExamsHandle().Handle(json_data)
    
    def find(self, json_data):
        return FindExam().find(json_data)
    
    def findTypeAll(self):
        return FindExam().findTypeExam()
        