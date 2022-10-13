#coding: utf-8

from django.shortcuts import render


def error404(request, exception):
    return render(request, 'django_tabler_ng/404.html', status=404)


def error500(request, exception):
    return render(request, 'django_tabler_ng/500.html', status=500)


def sign_in(request):
    return render(request, 'django_tabler_ng/singin.html', {})
