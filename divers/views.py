from django.shortcuts import render
from .functions import *


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

