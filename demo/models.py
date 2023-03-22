from django.db import models

# Create your models here.
class Employee(models.Model):
    Emp_id = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=200)
    Mobile_no = models.CharField(max_length=14)

    USERNAME_FIELD = 'Name'
    REQUIRED_FIELDS =[]


    def __str__(self):
        return self.Name