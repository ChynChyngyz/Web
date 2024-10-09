from django.shortcuts import render


def index(request):
    return render(request, 'web/index.html')


def registration(request):
    return render(request, 'web/registration.html')


def login(request):
    return render(request, 'web/login.html')
