from django.db import models

# Create your models here.

class Crampon(models.Model):
    brand = models.CharField(max_length=120)
    model = models.CharField(max_length=120)

class Short (models.Model):
    brand = models.CharField(max_length=120)
    model = models.CharField(max_length=120)

class Shirt(models.Model):
    brand = models.CharField(max_length=120)
    model = models.CharField(max_length=120)

class Equipment(models.Model):
    SIZE_OPTIONS = (
        ('XS','XS'),
        ('S','S'),
        ('M','M'),
        ('L','L'),
        ('XL','XL'),
        ('XXL','XXL')
    )
    crampon = models.ManyToManyRel(Crampon,to='crampon')
    crampon_size =models.PositiveSmallIntegerField(default=0)
    short = models.ManyToManyRel(Short,to='short')
    short_size =models.CharField(max_length=6,choices=SIZE_OPTIONS)
    shirt = models.ManyToManyRel(Shirt,to='shirt')
    shirt_size =models.CharField(max_length=6,choices=SIZE_OPTIONS)