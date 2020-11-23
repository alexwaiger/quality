# -*- coding: utf-8 -*-
from django.views.generic import ListView
from django.shortcuts import render

from .models import Casino

class ListCasinoView(ListView):

      model = Casino
      template_name = 'home.html'

def home(request):
    casino_list = Casino.objects.order_by("-rating")
    numbers = [8,2,3,0,9,8,0]
    context = {'casino_list': casino_list, 'numbers': numbers }
    return render(request, 'home.html', context)