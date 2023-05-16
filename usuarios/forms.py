from django import forms


class LoginForm(forms.Form):
    nome_login = forms.CharField(
        label='Nome de login',
        required=True,
        max_length=100,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Ex.: João Silva'
            }
        )
    )
    senha = forms.CharField(
        label='Senha',
        required=True,
        max_length=70,
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Digite sua senha'
            }
        ),
    )


class CadastroForm(forms.Form):
    nome_cadastro = forms.CharField(
        label='Nome completo',
        required=True,
        max_length=100,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Ex.: João Silva'
            }
        )
    )
    email = forms.CharField(
        label='Email',
        required=True,
        max_length=100,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Ex.: joaosilva@xpto.com'
            }
        )
    )
    senha = forms.CharField(
        label='Senha',
        required=True,
        max_length=70,
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Digite sua senha',
            }
        ),
    )
    confirme_senha = forms.CharField(
        label='Confirmação de senha',
        required=True,
        max_length=70,
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Digite sua senha mais uma vez',
            }
        ),
    )
