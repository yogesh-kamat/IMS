from django import forms

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(min_length=6,widget=forms.PasswordInput())