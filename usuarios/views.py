from django.shortcuts import render
from django.views import View
from usuarios.forms import LoginForm, CadastroForm

class Login(View):
    def get(self, request):
        return render(request, 'usuarios/login.html', {'form': LoginForm()})


class Cadastro(View):
    def get(self, request):
        return render(request, 'usuarios/cadastro.html', {'form': CadastroForm()})
