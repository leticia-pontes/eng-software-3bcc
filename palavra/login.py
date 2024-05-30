from django import forms

class LoginForm(forms.Form):
    usuario = forms.CharField(max_length=40)
    senha = forms.CharField(max_length=30, widget=forms.PasswordInput)