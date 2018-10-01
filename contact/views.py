# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from .models import Contact
from .forms import ContactForm
from django.http import JsonResponse
# Create your views here.


def create(request):

    form=ContactForm()
    return render(request,'create.html',{'form':form})


def saveContact(request):
    data={}
    if request.method == 'POST':
        form=ContactForm(request.POST)
        if form.is_valid():
            form.save()
            data = {
                'msg': 'Form submitted Successfully'
            }
        else:
            data = {
                'msg': 'Please fill up all the data!'
            }

    return JsonResponse(data)