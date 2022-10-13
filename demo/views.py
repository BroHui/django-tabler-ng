#coding: utf-8

from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required
def index(request):
    return render(request, 'demo/index.html', {})


@login_required
def blank_page(request):
    return render(request, 'demo/blank.html', {})