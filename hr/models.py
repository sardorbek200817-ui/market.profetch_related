from django.db import models
from django.utils import timezone

MONTHS = (
    ('1', "January"),
    ('2', "February"),
    ('3', "March"),
    ('4', "April"),
    ('5', "May"),
    ('6', "June"),
    ('7', "July"),
    ('8', "August"),
    ('9', "September"),
    ('10', "October"),
    ('11', "November"),
    ('12', "December"),
)


# Workers ishchilar
class Workers(models.Model):
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    phone_number = models.CharField(max_length=15)
    profession = models.CharField(max_length=30)    



class Salary(models.Model):
    workers = models.ForeignKey("Workers" , on_delete=models.CASCADE)
    month = models.CharField(choices=MONTHS)
    salary_sum = models.PositiveBigIntegerField()
    data = models.DateField(default=timezone.now)

    






















