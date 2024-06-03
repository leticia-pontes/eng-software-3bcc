# forms.py
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django import forms
from .models import Usuario

class LoginForm(AuthenticationForm):
    username = forms.CharField(label='Nome de Usuário', widget=forms.TextInput(attrs={
        'placeholder': 'Nome de Usuário',
        'required': 'required',
        'style': 'font-size: 24px; color: var(--borda-campo-letra); opacity: 0.22; color: black'
    }))
    password = forms.CharField(label='Senha', widget=forms.PasswordInput(attrs={
        'placeholder': 'Senha',
        'required': 'required',
        'style': 'font-size: 24px; color: var(--borda-campo-letra); opacity: 0.22; color: black'
    }))

    error_messages = {
        'invalid_login': (
            "Por favor, entre com um usuário e senha corretos. "
            "Note que ambos os campos diferenciam maiúsculas e minúsculas."
        ),
        'inactive': ("Esta conta está inativa."),
    }

class CadastroForm(UserCreationForm):
    email = forms.EmailField(label='E-mail', widget=forms.EmailInput(attrs={
        'placeholder': 'E-mail',
        'class': 'form-control'
    }))
    username = forms.CharField(label='Nome de Usuário', widget=forms.TextInput(attrs={
        'placeholder': 'Nome de Usuário',
        'class': 'form-control'
    }))
    password1 = forms.CharField(label='Senha', widget=forms.PasswordInput(attrs={
        'placeholder': 'Senha',
        'class': 'form-control'
    }))
    password2 = forms.CharField(label='Confirme a Senha', widget=forms.PasswordInput(attrs={
        'placeholder': 'Confirme a Senha',
        'class': 'form-control'
    }))

    class Meta(UserCreationForm.Meta): 
        model = Usuario
        fields = ['username', 'email', 'password1', 'password2']

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if Usuario.objects.filter(email=email).exists():
            raise forms.ValidationError('Este e-mail já está cadastrado!')
        return email

class UserInfoForm(forms.ModelForm):

    foto_perfil = forms.ImageField(widget=forms.FileInput())

    username = forms.CharField(label='Nome de Usuário', widget=forms.TextInput(attrs={
        'placeholder': 'Nome de Usuário',
        'class': 'form-control'
    }))
    email = forms.EmailField(label='E-mail', widget=forms.EmailInput(attrs={
        'placeholder': 'E-mail',
        'class': 'form-control'
    }))
    password1 = forms.CharField(label='Senha', widget=forms.PasswordInput(attrs={
        'placeholder': 'Senha',
        'class': 'form-control'
    }))

    class Meta:
        model = Usuario
        fields = ['username', 'email', 'foto_perfil']

    def __init__(self, *args, **kwargs):
        super(UserInfoForm, self).__init__(*args, **kwargs)
        self.fields['foto_perfil'].widget.attrs.update({
            'accept': 'image/*',
            'class': 'form-control-file'
        })