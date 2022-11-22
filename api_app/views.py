from django.shortcuts import render
from . import forms
from requests import Session
import json
from dotenv import load_dotenv
import os
from django.http import HttpResponseRedirect
from . import models
from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin

load_dotenv()

SECRET_KEY = os.getenv('SECRET_KEY')

def api(request):
    url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest'
    
    
    headers = {
        'Accepts': 'application/json',
        'X-CMC_PRO_API_KEY': SECRET_KEY
    }
    session = Session()
    session.headers.update(headers)
    
    info = "Ceci est un bug"
    form = forms.ApiForm(request.POST or None)

    if request.method =="POST" :
        
        if form.is_valid() :
            response = session.get(url, params=form.cleaned_data)
            print(form.cleaned_data)
            form.save()
            info = json.loads(response.text)
            return render(request, 'api_app/formulaire.html', context = {'form' : form, "info": info})

    return render(request, 'api_app/formulaire.html', context = {'form' : form})