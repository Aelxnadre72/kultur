from random import choices
from tkinter import CASCADE
from django.db import models
from django.utils.translation import gettext as _

# Create your models here.
class User(models.Model):

    class Experience(models.IntegerChoices):
        BEGINNER = '1', _('Beginner')
        MEDIOCRE = '2', _('Mediocre')
        VETERAN = '3', _('Veteran')

    firstName = models.CharField(max_length=100, blank = False)
    surname = models.CharField(max_length=100, blank = False)
    phoneNumber = models.TextField(primary_key=True)
    age = models.IntegerField(blank = False)
    experience = models.IntegerField(choices=Experience.choices, blank = False)
    location = models.TextField(blank = False)
    password = models.TextField(blank = False)
    isAdmin = models.BooleanField(default=False)

    def __str__(self):
        return self.firstName

class Event(models.Model):

    organizer = models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE)

    DIFFICULTY = (
        ('1', 'Lett'),
        ('2', 'Middels'),
        ('3', 'Vankselig')
    )

    AREA = (
        ('1', 'Trondheim'),
        ('2', 'Oslo'),
        ('3', 'Stavanger'),
        ('4', 'Bergen')
    )
    
    eventID = models.CharField(max_length=1, primary_key=True)
    eventName = models.CharField(max_length=100, blank = False)
    eventDate = models.DateTimeField()
    eventDifficulty = models.CharField(max_length=1, choices=DIFFICULTY)
    eventDescription = models.TextField()
    eventArea = models.CharField(max_length=1, choices=AREA, default='1', blank=False)
    eventLocation = models.CharField(max_length=100)
    eventSize = models.IntegerField(blank = False, default=0)
    hours = models.IntegerField()
    eventParticipants = models.TextField(default="")

class CommercialUser(models.Model):

    orgNumber = models.TextField(primary_key=True)
    orgName = models.CharField(max_length=100, blank = False, unique=True)
    location = models.TextField(blank = False)
    password = models.TextField(blank = False)
    isAdmin = models.BooleanField(default=False)

    def __str__(self):
        return self.orgName
    