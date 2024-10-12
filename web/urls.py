from django.urls import path
from . import views

app_name = 'web'

urlpatterns = [
    path('', views.index, name="index"),
    path('auth', views.auth, name='auth'),
    path('registration/', views.registration_view, name='registration'),
    # path('registration', views.registration, name="registration"),
    # path('login', views.login, name="login")
]