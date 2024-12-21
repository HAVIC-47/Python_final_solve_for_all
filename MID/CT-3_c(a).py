'''class Person:
     def __init__(self, nid,email, first_name, last_name):
          self.nid = nid
          self.email = email
          self.first_name = first_name
          self.last_name = last_name
     
     def  display_full_name(self):
          return self.first_name + " " + self.last_name + " " + self.nid + " " + self.email
     print(display_full_name("Alice", "Smith")) '''  

class Course:
     def __init__(self,course_name):
          self.course_name=course_name
     
class OnlineCourse(Course):
     def __init__(self, course_name, platform):
          super().__init__(course_name)
          self.platform=platform
     def display_course_info(self):
          print(f"Course name: {self.course_name} platfrom : {self.platform}")

online_course=OnlineCourse("Python", "Coursera")
online_course.display_course_info()
          