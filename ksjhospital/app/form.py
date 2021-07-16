from django.core import validators
from django import forms
from django.forms import ModelForm
from django.db.models import fields
from .models import appointment


class Patientappointment(forms.ModelForm):
    class meta :
          model = appointment
          field = [ 'patient_name', 'Age', 'oppintment_Date', 'Doctor']
        #   exclude = ['id' ,]