from django.contrib.auth.forms import UserCreationForm
from .models import User
from django import forms

class UserCreationFromCustom(UserCreationForm):
    
    class Meta(UserCreationForm.Meta) :
        model = User

        fields = ['username', 'password1', 'password2', 'email', 'birth_date']