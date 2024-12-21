def classify_grade(grade):
     if grade >= 90:
          return "A"
     elif grade >= 80:
          return "B"
     elif grade >= 70:
          return "C"
     elif grade >= 60:
          return "D"
     else:
          return "F"
print(classify_grade(85)) 

def find_total_marks(students, name):
     '''for key in students.keys():
          if key == name:
               return students[key]
     return "Student does not exist" '''

     if name in students:
          return students[name]
     return "Student does not exist"

students_marks = {
    "Alice": 85,
    "Bob": 92,
    "Charlie": 78,
    "David": 88
}

print(find_total_marks(students_marks, "David"))