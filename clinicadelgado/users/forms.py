#from accounts.models import Profile
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import get_user_model
from .models import Usuario
User = get_user_model()

class EditProfileForm(forms.ModelForm):
    fullname = forms.CharField(
        widget=forms.TextInput(attrs={
            'class':'shadow-sm focus:ring-indigo-500 dark:bg-dark-third dark:text-dark-txt focus:border-indigo-500 block w-full sm:text-sm border-gray-300 rounded-md',
        })
    )
    email = forms.CharField(
        widget=forms.TextInput(attrs={
            'class':'shadow-sm focus:ring-indigo-500 dark:bg-dark-third dark:text-dark-txt focus:border-indigo-500 block w-full sm:text-sm border-gray-300 rounded-md',
        })
    )
    telefono = forms.CharField(
        widget=forms.TextInput(attrs={
            'class':'shadow-sm focus:ring-indigo-500 dark:bg-dark-third dark:text-dark-txt focus:border-indigo-500 block w-full sm:text-sm border-gray-300 rounded-md',
        })
    )

    class meta:
        model = Usuario
        fiels = ('full_name','direccion','telefono')

class LoginForm(forms.Form):
    username= forms.CharField(label="Nombre de usuario",
                               widget=forms.TextInput(attrs={'placeholder':'nombre de usuario'}))
    password= forms.CharField(widget=forms.PasswordInput)

class RegisterForm(UserCreationForm):
       class Meta:
        model=Usuario
        fields =['username','full_name','email','telefono','password1','password2']

class ResetForm(UserCreationForm):
       class Meta:
        model=Usuario
        fields =['email']


