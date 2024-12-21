from django.db import models

from django.db import models

class User(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    date_joined = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(null=True, blank=True)
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

class UserProfile(models.Model):
    id = models.AutoField(primary_key=True)
    phone_no = models.CharField(max_length=15)
    profile_picture = models.ImageField(upload_to='profiles/', null=True, blank=True)
    date_of_birth = models.DateField()
    user = models.OneToOneField(User, on_delete=models.CASCADE)

class Student(models.Model):
    student_id = models.AutoField(primary_key=True)
    cgpa = models.FloatField()
    semester = models.CharField(max_length=10)
    user_profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE)

class VCAward(models.Model):
    id = models.AutoField(primary_key=True)
    session = models.CharField(max_length=50)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)

class Teacher(models.Model):
    id = models.AutoField(primary_key=True)
    designation = models.CharField(max_length=100)
    user_profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE)

class Course(models.Model):
    id = models.AutoField(primary_key=True)
    code = models.CharField(max_length=10, unique=True)
    name = models.CharField(max_length=100)

class AssignedCourse(models.Model):
    id = models.AutoField(primary_key=True)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    session = models.CharField(max_length=50)


# spring_22_3(b)

Students=Student.objects.filter(semester= '3-1',cgpa__gte=3.5).values('student_id', flat = True)
print(list(Students))

emails=User.objects.filter(
    UserProfile__Student__vcaward__session='spring_2021'
).values_list('email', flat=True)
print(list(emails))