from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django import forms


class LoginForm (AuthenticationForm): 
    username = forms.CharField(widget = forms.TextInput (attrs = {
    'placeholder': 'Your username',
    'class':'form-control',
    }))
    
    password = forms.CharField(widget = forms.PasswordInput (attrs = {
        'placeholder': 'Your password',
        'class': 'form-control',
    }))
    
class RegisterForm(UserCreationForm):  
    username = forms.CharField(widget=forms.TextInput(attrs={  
            'placeholder': 'Your username',  
            'class': 'form-control',  
    }))  
    email = forms.EmailField(widget=forms.EmailInput(attrs={  
            'placeholder': 'Your email',  
            'class': 'form-control',  
    }))  
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={  
            'placeholder': 'Your password',  
            'class': 'form-control',  
            'id': 'inputPW1'  
    }))  
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={  
            'placeholder': 'Repeat password',  
            'class': 'form-control',  
            'id': 'inputPW2'  
    })) 
    
