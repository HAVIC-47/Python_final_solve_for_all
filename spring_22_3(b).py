# spring_22_3(b)

Students=Student.objects.filter(semester= '3-1',cgpa__gte=3.5).values('student_id', flat = True)
print(list(Students))

emails=User.objects.filter(
    UserProfile__Student__vcaward__session='spring_2021'
).values_list('email', flat=True)
print(list(emails))