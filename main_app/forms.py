from django.forms import ModelForm
from django import forms
from .models import Feeding
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class FeedingForm(ModelForm):
  class Meta:
    model = Feeding
    fields = ['date', 'meal']

class SignupForm(UserCreationForm):
  class Meta:
    model = User
    fields = ['username', 'first_name', 'last_name', 'email']