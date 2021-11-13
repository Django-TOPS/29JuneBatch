from django import forms
from django.db import models
from django.db.models import fields
from .models import signup_master,userform

class SignupForm(forms.ModelForm):
    class Meta:
        model=signup_master
        fields='__all__'

class UserFormData(forms.ModelForm):
    class Meta:
        model=userform
        fields='__all__'