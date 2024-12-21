from django.db import models

class person(models.Model):
     phone_number=models.CharField(max_leanth=15)
     email_address=models.CharField(unique=True)
     name=models.CharField(max_length=100)

     def __str__(self):
          return self.name
     
class Address(models.Model):
     person=models.ForeignKey(person, on_delete=models.CASCADE ,related_name="address")
     city=models.CharField(max_length=100)
     state=models.CharField(max_length=20)
     postal_code=models.CharField(max_length=4)
     country=models.CharField(max_length=20)

     def __str__(self):
          return f"{self.city}, {self.state}, {self.country}"


from django import forms
from .models import *

class AddressForm(forms.ModelForm):
     class Meta:
          model=Address
          fields=["city","state","postal_code","country"]

def create_address(request):
     if request.method=="POST":
          form=AddressForm(request.POST)
          if form.is_valid():
               Address=form.save(commit=False)
               Address.person=request.user.person
               Address.save
               return Address
          else:
               form=AddressForm()

          return form

