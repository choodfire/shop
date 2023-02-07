from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm
from django import forms
# from django.contrib.auth.models import User
from .models import CustomUser

class RegistrationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ["username", "password1", "password2"]

class UserChangeNameForm(ModelForm):
    class Meta:
        model = CustomUser
        fields = ('username',)
        labels = {
            'username': '',
        }
        # widgets = {
        #     'username': forms.Textarea(),
        #     'profile_picture': forms.ImageField(),
        # }

class UserChangePFPForm(ModelForm):
    class Meta:
        model = CustomUser
        fields = ('profile_picture', )
        labels = {
            'profile_picture': '',
        }
        # widgets = {
        #     'username': forms.Textarea(),
        #     'profile_picture': forms.ImageField(),
        # }
