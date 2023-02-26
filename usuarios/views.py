from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


def Cadastro(request):
    return render(request, 'cadastro.html')


def Login(request):
    if request.method == "GET":
        return render(request, 'login.html')

    usuario = request.POST.get('usuario')
    senha = request.POST.get('senha')

    user = authenticate(username=usuario, password=senha)

    if user:
        login(request, user)
        return HttpResponse('autenticado')

    return HttpResponse('falhou')


@login_required
def AlgumaCoisa(request):
    return HttpResponse('Deu certo')


def Logout(request):
    logout(request)
    return HttpResponse('Saiu')
