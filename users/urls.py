from django.urls import path
from .views import home, RegisterView, CustomLoginView, ResetPasswordView, ChangePasswordView, profile, CustomLogoutView

app_name = 'users'

urlpatterns = [
    path('', home, name='users-home'),
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', CustomLogoutView.as_view(), name='logout'),
    path('password_reset/', ResetPasswordView.as_view(), name='password_reset'),
    path('change_password/', ChangePasswordView.as_view(), name='change_password'),
    path('profile/', profile, name='users-profile'),
]
