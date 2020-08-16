from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class FieldOwner(models.Model):

    user = models.OneToOneField(User,on_delete=models.CASCADE,unique=True)
    company_name = models.CharField(max_length=120)
    rating = models.PositiveSmallIntegerField(default=0)

    def __str__(self):
        return self.user.username



class Customer(models.Model):
    GENDER_OPTIONS = (
        ('Male','Male'),
        ('Female','Female'),
    )
    POSITION_OPTIONS = (
        ('Goal Keeper','Goal Keeper'),
        ('Defence','Defence'),
        ('Midfield','Midfield'),
        ('Striker','Striker'),
    )

    TEAM_OPTIONS = (
        ('FB','FB'),
        ('GS', 'GS'),
        ('BJK', 'BJK'),
        ('TS', 'TS'),
        ('Başakşehir', 'Başakşehir'),
        ('Bursa', 'Bursa'),
        ('GB', 'GB'),
        ('AG', 'AG'),
        ('Antalya', 'Antalya'),
        ('Antep', 'Antep'),
        ('Malatya', 'Malatya'),
        ('Kayseri', 'Kayseri'),
        ('Alanya', 'Alanya'),
        ('Göztepe', 'Göztepe'),
        ('Akhisar', 'Akhisar'),
        ('Hatay', 'Hatay'),
        ('Rize', 'Rize'),
        ('Sivas', 'Sivas'),
        ('Konya', 'Konya'),
        ('Kasımpaşa', 'Kasımpaşa'),
        ('Denizli', 'Denizli'),
        ('Erzurum', 'Erzurum'),
        ('Karabük', 'Karabük'),
        ('Eskişehir', 'Eskişehir'),
    )


    user = models.OneToOneField(User, on_delete=models.CASCADE,unique=True)
    age = models.PositiveSmallIntegerField(blank=True,null=True)
    super_lig_team=models.CharField(max_length=50, choices=TEAM_OPTIONS,blank=True, null=True)
    gender = models.CharField(max_length=25,choices=GENDER_OPTIONS,blank=True,null=True)
    position = models.CharField(max_length=25,choices=POSITION_OPTIONS,blank=True,null=True)
    ave_rating = models.PositiveSmallIntegerField(default=0)
    registration_date = models.DateTimeField(auto_now_add=True)
    last_active_date = models.DateTimeField(blank=True,null=True)

    def __str__(self):
        return "Customer_"+self.user.username


class Referee(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, unique=True)
    ave_rating = models.PositiveSmallIntegerField(default=0)
    registration_date = models.DateTimeField(auto_now_add=True)
    last_active_date = models.DateTimeField(blank=True, null=True)


    def __str__(self):
        return "Refree_"+self.user.username