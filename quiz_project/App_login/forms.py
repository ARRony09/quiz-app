from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm 

class SignUpNewUser(UserCreationForm):
    username=forms.CharField(label="Username",required=True)
    email=forms.EmailField(label="Email Address")
    class Meta:
        model=User
        fields=('username','email','password1','password2')