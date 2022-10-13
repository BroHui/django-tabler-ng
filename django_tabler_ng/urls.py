from cgitb import handler
from django.urls import path
from .views import *
from django.contrib.auth import views as auth_views

app_name = 'django_tabler_ng'

urlpatterns = [
    path('sign_in/', auth_views.LoginView.as_view(template_name='django_tabler_ng/signin.html'), name='sign_in'),
    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('sign_out/', auth_views.LogoutView.as_view(template_name='django_tabler_ng/signout.html'), name='logout'),
]
