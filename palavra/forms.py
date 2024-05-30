from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import Usuario

class LoginForm(forms.Form):
    email = forms.EmailField(widget=forms.EmailInput(attrs={
        'name': 'email',
        'id': 'email',
        'placeholder': 'E-mail',
        'required': 'required',
        'style': 'font-size: 24px; color: var(--borda-campo-letra); opacity: 0.22; color: black'
    }))
    senha = forms.CharField(widget=forms.PasswordInput(attrs={
        'name': 'senha',
        'id': 'senha',
        'placeholder': 'Senha',
        'required': 'required',
        'style': 'font-size: 24px; color: var(--borda-campo-letra); opacity: 0.22; color: black'
    }))


class CadastroForm(forms.ModelForm):
    nome = forms.CharField(widget=forms.TextInput(attrs={
        'name': 'nome',
        'id': 'nome',
        'placeholder': 'Usuário',
        'required': 'required',
        'style': 'font-size: 24px; color: var(--borda-campo-letra); opacity: 0.22; color: black'
    }))
    email = forms.EmailField(widget=forms.EmailInput(attrs={
        'name': 'email',
        'id': 'email',
        'placeholder': 'E-mail',
        'required': 'required',
        'style': 'font-size: 24px; color: var(--borda-campo-letra); opacity: 0.22; color: black'
    }))
    senha = forms.CharField(widget=forms.PasswordInput(attrs={
        'name': 'senha',
        'id': 'senha',
        'placeholder': 'Senha',
        'required': 'required',
        'style': 'font-size: 24px; color: var(--borda-campo-letra); opacity: 0.22; color: black'
    }))
    # confirma_senha = forms.CharField(widget=forms.PasswordInput(attrs={
    #     'name': 'confirma_senha',
    #     'id': 'confirma_senha',
    #     'placeholder': 'Senha',
    #     'required': 'required',
    #     'style': 'font-size: 24px; color: var(--borda-campo-letra); opacity: 0.22; color: black'
    # }))

    class Meta:
        model = Usuario
        fields = ['nome', 'email', 'senha']

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if Usuario.objects.filter(email=email).exists():
            raise forms.ValidationError('Este e-mail já está cadastrado!')
        return email

    def clean(self):
        cleaned_data = super().clean()
        senha = cleaned_data.get('senha')
        confirma_senha = cleaned_data.get('confirma_senha')

        if senha and confirma_senha and senha != confirma_senha:
            raise forms.ValidationError('As senhas não são iguais!')

        return cleaned_data
