# coding=utf-8
from django.shortcuts import render


"""
Vista principal
"""
def index(request):
    context = {

    }
    return render(request, 'SGRD/index.html', context)