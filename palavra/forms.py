from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django import forms
from .models import Usuario

class LoginForm(AuthenticationForm):
    username = forms.CharField(label='Nome de Usuário', widget=forms.TextInput(attrs={
        'placeholder': 'Nome de Usuário',
        'required': 'required',
        'style': 'font-size: 24px; color: black',
        'class': 'login-form',
    }))
    password = forms.CharField(label='Senha', widget=forms.PasswordInput(attrs={
        'placeholder': 'Senha',
        'required': 'required',
        'style': 'font-size: 24px; color: black',
        'class': 'login-form',
    }))

    error_messages = {
        'invalid_login': (
            "Por favor, entre com um usuário e senha corretos."
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

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if Usuario.objects.filter(username=username).exists():
            raise forms.ValidationError('Este nome de usuário já está em uso. Por favor, escolha outro.')
        return username

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if Usuario.objects.filter(email=email).exists():
            raise forms.ValidationError('Este e-mail já está cadastrado. Por favor, use outro e-mail.')
        return email

class UserInfoForm(forms.ModelForm):
    foto_perfil = forms.ImageField(label='Foto de Perfil', widget=forms.FileInput(attrs={
        'accept': 'image/*',
        'class': 'form-control-file'
    }))

    class Meta:
        model = Usuario
        fields = ['username', 'email', 'foto_perfil']

    def clean_email(self):
        email = self.cleaned_data.get('email')
        instance = getattr(self, 'instance', None)
        if Usuario.objects.exclude(pk=instance.pk).filter(email=email).exists():
            raise forms.ValidationError('Este e-mail já está cadastrado.')
        return email
