from rest_framework import serializers
from .models import User, Event, CommercialUser

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['firstName', 'surname', 'phoneNumber', 'age', 'experience', 'location', 'password', 'isAdmin']


class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ['eventID', 'eventName', 'eventDate', 'eventDifficulty', 'eventDescription', 'eventArea', 'eventLocation', 'eventSize', 'hours', 'eventParticipants']


class CommercialUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CommercialUser
        fields = ['orgNumber', 'orgName', 'location', 'password', 'isAdmin']
