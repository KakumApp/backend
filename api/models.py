from django.db import models

# Create your models here.


class Country(models.Model):
    name = models.CharField(max_length=50)


class Place(models.Model):
    country = models.ForeignKey(Country, related_name='places')
    name = models.CharField(max_length=50, unique=True)


class Target(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    other_name = models.CharField(max_length=50, null=True)
    phone_no = models.CharField(max_length=20)
    photo = models.TextField()
    places = models.ManyToManyField(Place, null=False)


