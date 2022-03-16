from django import forms
from .models import info

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