from django import forms
from django.core.validators import MaxLengthValidator
from django.db.models.fields import GenericIPAddressField
from django.forms.formsets import MAX_NUM_FORM_COUNT
from django.forms.widgets import RadioSelect, Select
class MembershipForm(forms.Form):
    Gender =[('M', 'Male'),('F', 'Female')]
    Baptised =[('Y', 'Yes'),('N', 'No')]
    Rescues=(('Y', 'Yes'),('N', 'No'))
    full_name = forms.CharField(max_length=100)
    gender= forms.ChoiceField(widget=RadioSelect, choices=Gender)
    phone_number = forms.IntegerField()
    physical_address = forms.CharField(max_length=50)
    baptised = forms.ChoiceField(widget=Select, choices=Baptised)
    rescued_ggh = forms.ChoiceField(widget=Select, choices=Rescues)