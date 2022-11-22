from django.shortcuts import render
from .functions import *
from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from .forms import UserCreationFromCustom


def home_page(request):
    weekdays = [
        'lundi',
        'mardi',
        'mercredi',
        'jeudi',
        'vendredi',
        'samedi',
        'dimanche',
    ]

    context = {
        "test" : multiplicate_by_5(5),
        "weekdays":weekdays
    }
    # import pudb;pu.db()

    return render(request, 'divers/home_page.html', context = context)

class SignupPage(CreateView):
    form_class= UserCreationFromCustom
    success_url= reverse_lazy('login')
    template_name= 'registration/signup.html'