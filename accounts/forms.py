from django import forms
from .models import accounts_patientmodel

# Doctors login form
class LoginDoctorsForm(forms.ModelForm):
    email = forms.CharField(max_length=254, required=True, widget=forms.EmailInput())
    
    class Meta:
        model = accounts_patientmodel
        fields = ['email','password']
