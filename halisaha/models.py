from django.db import models
from django.contrib.auth.models import User
from accounts.models import *
# Create your models here.


class Address(models.Model):


    user = models.ForeignKey(User, on_delete=models.CASCADE,default=1)
    name = models.CharField(max_length=120)
    street = models.CharField(max_length=250)
    region = models.CharField(max_length=120)
    city = models.CharField(max_length=120)
    country = models.CharField(max_length=120)
    latitude = models.DecimalField(max_digits=9, decimal_places=6,default=0,blank=True,null=True)
    longitude =models.DecimalField(max_digits=9, decimal_places=6,default=0,blank=True,null=True)
    zip_code = models.PositiveIntegerField()


    def __str__(self):
        return self.name


class Field(models.Model):
    CAPABILITY_OPTIONS = (
        ('Sıcak Icecek', 'Sıcak Icecek'),
        ('Soguk Icecek', 'Soguk Icecek'),
        ('Yiyecek', 'Yiyecek'),
        ('WC', 'WC'),
        ('Dus', 'Dus'),
        ('Soyunma Kabini', 'Soyunma Kabipermisni'),
        ('Kamera', 'Kamera'),
        ('Kapalı', 'Kapalı'),

    )
    owner = models.ForeignKey(FieldOwner,on_delete=models.CASCADE)
    name = models.CharField(max_length=150)
    address = models.OneToOneField(Address,on_delete=models.CASCADE)
    capabilities = models.CharField(max_length=500,choices=CAPABILITY_OPTIONS)

    is_active = models.BooleanField(default=False)

    def __str__(self):
        return self.owner.user.username+"_"+self.name


class Agenda(models.Model):
    date = models.DateField(blank=False, null=False)
    field = models.ForeignKey(Field, on_delete=models.CASCADE)

    active_0 = models.BooleanField(default=0)
    active_1 = models.BooleanField(default=0)
    active_2 = models.BooleanField(default=0)
    active_3 = models.BooleanField(default=0)
    active_4 = models.BooleanField(default=0)
    active_5 = models.BooleanField(default=0)
    active_6 = models.BooleanField(default=0)
    active_7 = models.BooleanField(default=0)
    active_8 = models.BooleanField(default=0)
    active_9 = models.BooleanField(default=0)
    active_10 = models.BooleanField(default=0)
    active_11 = models.BooleanField(default=0)
    active_12 = models.BooleanField(default=0)
    active_13 = models.BooleanField(default=0)
    active_14 = models.BooleanField(default=0)
    active_15 = models.BooleanField(default=0)
    active_16 = models.BooleanField(default=0)
    active_17 = models.BooleanField(default=0)
    active_18 = models.BooleanField(default=0)
    active_19 = models.BooleanField(default=0)
    active_20 = models.BooleanField(default=0)
    active_21 = models.BooleanField(default=0)
    active_22 = models.BooleanField(default=0)
    active_23 = models.BooleanField(default=0)

    reserved_0 = models.BooleanField(default=0)
    reserved_1 = models.BooleanField(default=0)
    reserved_2 = models.BooleanField(default=0)
    reserved_3 = models.BooleanField(default=0)
    reserved_4 = models.BooleanField(default=0)
    reserved_5 = models.BooleanField(default=0)
    reserved_6 = models.BooleanField(default=0)
    reserved_7 = models.BooleanField(default=0)
    reserved_8 = models.BooleanField(default=0)
    reserved_9 = models.BooleanField(default=0)
    reserved_10 = models.BooleanField(default=0)
    reserved_11 = models.BooleanField(default=0)
    reserved_12 = models.BooleanField(default=0)
    reserved_13 = models.BooleanField(default=0)
    reserved_14 = models.BooleanField(default=0)
    reserved_15 = models.BooleanField(default=0)
    reserved_16 = models.BooleanField(default=0)
    reserved_17 = models.BooleanField(default=0)
    reserved_18 = models.BooleanField(default=0)
    reserved_19 = models.BooleanField(default=0)
    reserved_20 = models.BooleanField(default=0)
    reserved_21 = models.BooleanField(default=0)
    reserved_22 = models.BooleanField(default=0)
    reserved_23 = models.BooleanField(default=0)



    #price_zero = models.PositiveSmallIntegerField(null=False,blank=False,default=0)
    price = models.PositiveSmallIntegerField(null=False,blank=False,default=0)

    #price_list = models.PositiveIntegerField(null=False,blank=False,default=0)




    def __str__(self):
        return self.field.name+"_"+str(self.date)

class FieldConfiguration(models.Model):
    field = models.OneToOneField(Field,related_name="configuration_field",on_delete=models.CASCADE)
    agenda_creation_day = models.PositiveSmallIntegerField(default=15)
    enabled = models.PositiveIntegerField(default=0)
    reserved_by_owner = models.PositiveIntegerField(default=0)
    price=models.PositiveSmallIntegerField(default=0)


class FieldOwnerDiscount(models.Model):
    field = models.OneToOneField(Field,on_delete=models.CASCADE,related_name="discount_field")
    day = models.PositiveSmallIntegerField()
    hours = models.PositiveIntegerField()
    discount_rate = models.PositiveSmallIntegerField()









class Reservation(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    agenda = models.ForeignKey(Agenda,on_delete=models.CASCADE)
    hour = models.PositiveSmallIntegerField()
    reservation_request_date = models.DateTimeField(blank=True,null=True)
    reservation_approval_date = models.DateTimeField(blank=True,null=True)
    reservation_cancel_date = models.DateTimeField(blank=True,null=True)
    canceled_by = models.ForeignKey(User,on_delete=models.CASCADE,blank=True,null=True)
    reservation_happened = models.BooleanField(default=False)

    def __str__(self):
        return self.customer.user.username+"_"+str(self.id)

class Comment(models.Model):
    owner = models.ForeignKey(User,on_delete=models.CASCADE)
    reservation = models.ForeignKey(Reservation,on_delete=models.CASCADE)
    rating = models.PositiveSmallIntegerField()
    text = models.CharField(max_length=500)

    def __str__(self):
        return self.owner.username+"_"+str(self.reservation.pk)

class Team(models.Model):
    name =models.CharField(max_length=150,unique=True)
    captain = models.OneToOneField(Customer,on_delete=models.CASCADE,related_name="cap")
    players = models.ForeignKey(Customer,on_delete=models.CASCADE,related_name="plyrs")
    total_match = models.PositiveSmallIntegerField(default=0)
    win_number = models.PositiveSmallIntegerField(default=0)
    lost_number =models.PositiveSmallIntegerField(default=0)
    score = models.PositiveIntegerField(default=0)
    anti_score = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.name

class Match(models.Model):
    reservation = models.OneToOneField(Reservation,on_delete=models.CASCADE)
    host_team = models.OneToOneField(Team,on_delete=models.CASCADE,related_name="host")
    guest_team = models.OneToOneField(Team,on_delete=models.CASCADE,related_name="guest")
    host_goal = models.PositiveSmallIntegerField(default=0,blank=True,null=True)
    guest_goal = models.PositiveSmallIntegerField(default=0,blank=True,null=True)
    referee = models.OneToOneField(Referee,on_delete=models.CASCADE,blank=True,null=True)

    def __str__(self):
        return "Reservation_"+self.reservation_id




class Goal (models.Model):
    match = models.ForeignKey(Match,on_delete=models.CASCADE)
    owner = models.OneToOneField(Customer,on_delete=models.CASCADE,related_name="owner")
    assist = models.OneToOneField(Customer,on_delete=models.CASCADE,blank=True,null=True,related_name="assist")
    approved = models.BooleanField(default=False)
    approved_by = models.ForeignKey(Customer,on_delete=models.CASCADE,related_name="approved_by")


class PlayerSearch(models.Model):
    POSITION_OPTIONS = (
        ('Goal Keeper','Goal Keeper'),
        ('Defence','Defence'),
        ('Midfield','Midfield'),
        ('Striker','Striker'),
    )
    reservation_no = models.ForeignKey(Reservation,on_delete=models.CASCADE)
    owner = models.ForeignKey(Customer,on_delete=models.CASCADE)
    position = models.CharField(max_length=120,choices=POSITION_OPTIONS,blank=True,null=True)
    creation_date = models.DateTimeField(auto_created=True)
    candidates = models.ManyToManyField(Customer,related_name="candi")
    accepted_candidate = models.ForeignKey(Customer,on_delete=models.CASCADE,related_name="winner_can")

class PlayerRating(models.Model):
    maker = models.ForeignKey(User,on_delete=models.CASCADE,related_name="rating_maker")
    rated_player = models.ForeignKey(User,on_delete=models.CASCADE,related_name="rated_player")
    reservation = models.ForeignKey(Reservation,on_delete=models.CASCADE,related_name="reserv")
    physic = models.PositiveSmallIntegerField()
    technic = models.PositiveSmallIntegerField()
    strike = models.PositiveSmallIntegerField()
    team_game = models.PositiveSmallIntegerField()
    red_card = models.PositiveSmallIntegerField(default=0)
    yellow_card = models.PositiveSmallIntegerField(default=0)