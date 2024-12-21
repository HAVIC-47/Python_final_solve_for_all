class Event:
     def __init__(self,event_name,location):
          self.event_name=event_name
          self.location=location 

     def display_event_details(self):
          print(f"the event name is {self.event_name} and the location is {self.location}")

event_1=Event("biye", "Xian")
event_1.display_event_details()

class Course:
    def __init__(self, course_name):
        self.course_name = course_name

class OnlineCourse(Course):
    def __init__(self, course_name, platform):
        super().__init__(course_name)
        self.platform = platform
          