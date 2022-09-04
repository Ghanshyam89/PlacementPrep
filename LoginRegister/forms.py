# from socket import fromshare
from django import forms

class RegistrationForm(forms.Form):
    first_name = forms.CharField(label='First name', 
                                max_length=100,
                                widget=forms.TextInput(attrs={
                                    'class':'form-control',
                                    'id':'registerFirstName'
                                }))
    last_name = forms.CharField(label='Last name',
                            max_length=100,
                            widget=forms.TextInput(attrs={
                                'class':'form-control',
                                'id':'registerLastName'
                            }))
    username = forms.CharField(label='Username',
                            max_length=100,
                            widget=forms.TextInput(attrs={
                                'class':'form-control',
                                'id':'registerUsername'
                            }))
    email = forms.CharField(label='Email',
                            max_length=100,
                            widget=forms.TextInput(attrs={
                                'class':'form-control',
                                'id':'registerEmail'
                            }))
    password = forms.CharField(label='Password',
                            max_length=100,
                            widget=forms.TextInput(attrs={
                                'class':'form-control',
                                'id':'registerPassword'
                            }))
    repeat_password =  forms.CharField(label='Repeat Password',
                            max_length=100,
                            widget=forms.TextInput(attrs={
                                'class':'form-control',
                                'id':'registerRepeatPassword'
                            }))
        
    
