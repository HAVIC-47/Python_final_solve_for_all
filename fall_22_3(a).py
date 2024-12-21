from django.db import models

class author(models.Model):
     name=models.CharField(max_length=123)
     photo=models.ImageField(upload_to='author/photos/')
     id=models.CharField(primary_key=True,max_length=123)

     def __str__(self):
          return self.name

    
class book(models.Model):
     name=models.CharField(max_length=123)
     genre=models.CharField(max_length=123)
     publication=models.DateField()
     author_id=models.ForeignKey(author,on_delete=models.CASCADE)
