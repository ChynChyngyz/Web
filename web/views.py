from django.shortcuts import render, redirect
from .forms import RegistrationForm


def index(request):
    return render(request, 'web/index.html')


def auth(request):
    return render(request, 'web/auth.html')


def registration_view(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('')
    else:
        form = RegistrationForm()

    return render(request, 'web/auth.html', {'form': form})

# def registration(request):
#     return render(request, 'web/registration.html')
#
#
# def login(request):
#     return render(request, 'web/login.html')