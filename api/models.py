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


class Intermediary(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    other_name = models.CharField(max_length=50, null=True)
    phone_no = models.CharField(max_length=20)
    photo = models.TextField()


class MeetingPoint(models.Model):
    intermediary = models.ForeignKey(Intermediary, related_name='meeting_points')
    name = models.CharField(max_length=50)
    location = models.CharField(max_length=100)
    gps_lat = models.CharField(max_length=50)
    gps_long = models.CharField(max_length=50)
    photo = models.TextField()


class MeetingTime(models.Model):
    meeting_point = models.ForeignKey(MeetingPoint, related_name='meeting_times')
    day = models.CharField(max_length=20)
    begin = models.CharField(max_length=10)
    end = models.CharField(max_length=10)