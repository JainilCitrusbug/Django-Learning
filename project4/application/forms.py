from dataclasses import field
from django import forms
from .models import info
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

# # Form API
# class StudentRegistrationForm(forms.Form):
#     name = forms.CharField()
#     email = forms.EmailField()
#     number = forms.CharField(max_length=10)
#     course = forms.CharField()

# Model Form
class StudentRegistrationForm(forms.ModelForm):
    class Meta:
        model = info
        fields = '__all__'

# class SignUp(UserCreationForm):
#     password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput)
#     class Meta:
#         model = User
#         fields = ['username', 'first_name', 'last_name', 'email']
#         labels = {'email' : 'Email'}
