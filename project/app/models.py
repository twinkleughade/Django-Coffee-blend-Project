from django.db import models

# Create your models here.
class student(models.Model):
    stu_name=models.CharField(max_length=50)
    stu_email=models.EmailField()
    stu_contact=models.IntegerField()
    stu_dob=models.DateField()
    stu_gender=models.CharField(max_length=50)
    stu_pass=models.CharField(max_length=50)

class Items(models.Model):
    item_name=models.CharField(max_length=20)
    item_des=models.CharField(max_length=20)
    item_price=models.IntegerField()
    





