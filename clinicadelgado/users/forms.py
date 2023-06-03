from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Usuario

class LoginForm(forms.Form):
    username= forms.CharField(label="Nombre de usuario",
                               widget=forms.TextInput(attrs={'placeholder':'nombre de usuario'}))
    password= forms.CharField(widget=forms.PasswordInput)

class RegisterForm(UserCreationForm):
       class Meta:
        model=Usuario
        fields =['username','full_name','email','telefono','password1','password2']