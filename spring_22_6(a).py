from django.db import models

class person(models.Model):
     first_name= models.CharField(max_length=50)
     last_name= models.CharField(max_length=50)
     date_of_birth= models.DateField()
     phone_no= models.CharField(max_length=15)

# forms.py:
class personForm(forms.ModelForm):
    class Meta:
        model= person
        fields= '__all__'

# views.py:

from django.shortcuts import render.redirect
from .forms import personForm

def register_person(request):
    if request.method=="POST":
        form =personForm(request.POST)
        if form.is_valid():
          form.save()
          return redirect('success')
     else:
          form=personForm()
     return render(request, 'home/register_person.html', {'form':form})

def success(request):
    return render(request, 'home/success.html')
# urls.py:
from django.urls import path
from django.contrib import admin
from home import views
urlpatterns = [
    path('admin/',admin.site.urls),
    path('rregister_person/', views.register_person, name='register_person'),
    path('success/', views.success, name='success')
]

# home.html:
<!DOCTYPE html>
<html>
<head>
    <title>Register Person</title>
<head>
<body>
     <h1>Register a Person</h1>
     <form method= "POST">
          {% csrf_token %}
          {{form.as_p}}
          <button type="submit">Register</button>
     </form>
</body>
</html>