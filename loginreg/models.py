from django.db import models
from django.core.validators import RegexValidator
from accounts.models import MyUser
from datetime import datetime, timedelta

# Create your models here.

class players(models.Model):
    user = models.OneToOneField(MyUser, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    pubg_name = models.CharField(max_length=20, unique=True)
    pubg_id = models.IntegerField(unique=True, primary_key=True)

    mobile_regex = RegexValidator(regex=r"^(?:\+88|01)?(?:\d{11})$", message="Phone number must be entered in the format: '+8801xxxxxxxxx' or '01xxxxxxxxx'. ")
    mobile = models.CharField(validators=[mobile_regex], max_length=14, unique=True)

    email = models.EmailField(unique=True)

    def __str__(self):
        return str(self.pubg_id)

class temp_player(models.Model):
    name = models.CharField(max_length=50)
    pubg_name = models.CharField(max_length=20)
    pubg_id = models.IntegerField()
    mobile = models.CharField(max_length=14)
    email = models.EmailField()
    password = models.CharField(max_length=20)

    verified = models.BooleanField(default=False)
    otp = models.CharField(max_length=6, unique=True)
    otp2 = models.CharField(max_length=6, blank=True,  null= True, unique=True)
    otp3 = models.CharField(max_length=6, blank=True,  null= True, unique=True)
    session = models.CharField(max_length=10, unique=True)
    exp_time = models.DateTimeField(default=datetime.now() + timedelta(minutes=5))

    def __str__(self):
        return str(self.pubg_id)