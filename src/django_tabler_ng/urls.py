from cgitb import handler
from django.urls import path
from .views import *
from django.urls import reverse_lazy
from django.contrib.auth import views as auth_views

app_name = 'django_tabler_ng'

urlpatterns = [
    path('sign_in/', auth_views.LoginView.as_view(
        template_name='django_tabler_ng/signin.html'), name='sign_in'),
    path('password_reset/', auth_views.PasswordResetView.as_view(),
         name='password_reset'),
    path('password_change/', auth_views.PasswordChangeView.as_view(
        template_name='django_tabler_ng/password_change.html',
        success_url = reverse_lazy('django_tabler_ng:password_change_done')), name='password_change'),
    path('password_change_done/', auth_views.PasswordChangeDoneView.as_view(
        template_name='django_tabler_ng/password_change_done.html'), name='password_change_done'),
    path('sign_out/', auth_views.LogoutView.as_view(
        template_name='django_tabler_ng/signout.html'), name='sign_out'),
]
