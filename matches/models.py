from django.db import models

# Create your models here.
class Match(models.Model):
    location = models.CharField(max_length=50)
    match_type = models.CharField(max_length=50)
    match_mode = models.CharField(max_length=50)
    match_time = models.TimeField()
    match_stats = (
        ('upcoming', 'UpComing'),
        ('open', 'Open'),
        ('full', 'Full'),
        ('running', 'Running'),
        ('over', 'Over')
    )
    match_status = models.CharField(choices=match_stats, max_length=10)

    def __str__(self):
        return str(self.id)
        
class Match_1_Player(models.Model):
    playerid = models.IntegerField()
    playername = models.CharField(max_length=20)
    paid_from = (
        ('account', 'Account'),
        ('bkash', 'Bkash')
    )
    paid_through = models.CharField(choices=paid_from, max_length=10)
    txnid = models.CharField(max_length = 20, blank=True,  null= True)

class Match_2_Player(models.Model):
    playerid = models.IntegerField()
    playername = models.CharField(max_length=20)
    paid_from = (
        ('account', 'Account'),
        ('bkash', 'Bkash')
    )
    paid_through = models.CharField(choices=paid_from, max_length=10)
    txnid = models.CharField(max_length = 20, blank=True,  null= True)
    
class Match_3_Player(models.Model):
    playerid = models.IntegerField()
    playername = models.CharField(max_length=20)
    paid_from = (
        ('account', 'Account'),
        ('bkash', 'Bkash')
    )
    paid_through = models.CharField(choices=paid_from, max_length=10)
    txnid = models.CharField(max_length = 20, blank=True,  null= True)
    
class Match_4_Player(models.Model):
    playerid = models.IntegerField()
    playername = models.CharField(max_length=20)
    paid_from = (
        ('account', 'Account'),
        ('bkash', 'Bkash')
    )
    paid_through = models.CharField(choices=paid_from, max_length=10)
    txnid = models.CharField(max_length = 20, blank=True,  null= True)
    
class Match_5_Player(models.Model):
    playerid = models.IntegerField()
    playername = models.CharField(max_length=20)
    paid_from = (
        ('account', 'Account'),
        ('bkash', 'Bkash')
    )
    paid_through = models.CharField(choices=paid_from, max_length=10)
    txnid = models.CharField(max_length = 20, blank=True,  null= True)
    
class Match_6_Player(models.Model):
    playerid = models.IntegerField()
    playername = models.CharField(max_length=20)
    paid_from = (
        ('account', 'Account'),
        ('bkash', 'Bkash')
    )
    paid_through = models.CharField(choices=paid_from, max_length=10)
    txnid = models.CharField(max_length = 20, blank=True,  null= True)
    
