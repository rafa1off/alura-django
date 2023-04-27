from django.shortcuts import render
from django.views import View
from .forms import LoginForm

class Login(View):
    def get(self, request):
        form = LoginForm()
        return render(request, 'usuarios/login.html', {'form': form})


class Cadastro(View):
    def get(self, request):
        return render(request, 'usuarios/cadastro.html')
