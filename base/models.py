from django.db import models

# Create your models here.


class Hms_guest(models.Model):
    guest_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone_no = models.IntegerField
    no_of_guest = models.IntegerField
    room_type = models.TextField
    check_in = models.DateField()
    payment_method = models.IntegerField
    check_out = models.DateField()

class Hms_emp(models.Model):
    employee_id = models.IntegerField
    employee_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone_no = models.IntegerField
