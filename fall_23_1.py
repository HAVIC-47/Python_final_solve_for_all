def pass_or_fail(grade_dict,passing_grade):
     passing_student=[]

     for student , grades in grade_dict.items():
          avarage_grade=sum(grades)/len(grades)
          if avarage_grade>=passing_grade:
               passing_student.append(student)

     return passing_student