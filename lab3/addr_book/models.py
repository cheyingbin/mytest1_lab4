from django.db import models
#from django.contrib.auth.models import User

class People(models.Model):
    user = models.CharField(max_length=30)
    name = models.CharField(max_length=30)
    number = models.CharField(max_length = 50)
    sex = models.BooleanField(default=True)
    phone = models.CharField(max_length=15)
    email = models.EmailField()
    address = models.CharField(max_length=50)
    qq = models.CharField(max_length=50)
    birthday = models.CharField(max_length=50)

class Author(models.Model):
    AuthorID = models.CharField(max_length = 30)
    Name = models.CharField(max_length = 30)
    Age = models.IntegerField()
    Country = models.CharField(max_length = 30)
    
class Book(models.Model):
    ISBN = models.CharField(max_length = 13)
    Title = models.CharField(max_length = 30)
    Author = models.ForeignKey(Author)
    Publisher = models.CharField(max_length = 30)
    PublishDate = models.CharField(max_length = 50)
    Price = models.FloatField()

