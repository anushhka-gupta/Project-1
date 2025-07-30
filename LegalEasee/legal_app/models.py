from django.db import models
from django.utils import timezone

class Feedback(models.Model):
    email=models.CharField(max_length=45,primary_key=True)
    name=models.CharField(max_length=55,null=False)
    rating=models.CharField(max_length=55,null=False)
    remark=models.TextField(default="")
    user_pic=models.CharField(max_length=255,default="")
    date=models.DateField(default=timezone.now)

class Contact(models.Model):
    email=models.CharField(max_length=45)
    name=models.CharField(max_length=55,null=False)
    phone=models.CharField(max_length=13,null=False)
    question=models.TextField()
    date=models.DateField(default=timezone.now)
    def __str__(self): #it represents object into string from self means object
        return self.name

class User(models.Model):
    name=models.CharField(max_length=60)
    email=models.EmailField(max_length=60,primary_key=True)
    password=models.CharField(max_length=45)
    phone=models.CharField(max_length=13)
    pic_name=models.FileField(upload_to="user_pic/",default="")
    def __str__(self):
        return self.name
    
class Advisor(models.Model):
    email=models.CharField(max_length=60,primary_key=True)
    password=models.CharField(max_length=45)
    name=models.CharField(max_length=60)
    qualification=models.CharField(max_length=100)
    gender=models.CharField(max_length=6)
    expirience=models.TextField()
    service_type=models.CharField(max_length=100)
    phone=models.CharField(max_length=15,default="9898989898")
    about_advisor=models.TextField()
    profile_pic=models.FileField(upload_to="advisor_pic/",default="")
    def __str__(self):
        return self.name
    
class Service(models.Model):
    service_type=models.CharField(max_length=100,primary_key=True)
    description=models.TextField(default="")
    service_pic=models.FileField(upload_to="service_pic/",default="")
