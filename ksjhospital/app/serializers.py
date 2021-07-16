from django.db import models
from django.db.models import fields
from rest_framework import serializers
from .models import appointment


class appointmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = appointment
        field = '__all__'
        exclude = ['id' ,]
        #fields = ['name', 'Age']



class timeslotSerializer(serializers.ModelSerializer):
    class Meta:
        model = appointment
        # field = '__all__'
        # exclude = ['id' ,]
        fields = [ 'timeslot']

    