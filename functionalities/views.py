from django.shortcuts import render
from.models import Functionalities
from django.views.generic import ListView, DetailView, CreateView
from django.urls import reverse_lazy

class FunctionalitiesListView(ListView):
    model = Functionalities
    template_name = "functionalities/functionalities_list.html"
    context_object_name = "functionalities_list"

class FunctionalitiesDetailView(DetailView):
    model = Functionalities
    template_name = "functionalities/functionalities_detail.html"

class FunctionalitiesCreateView(CreateView):
    model = Functionalities
    template_name = "functionalities/functionalities_create.html"
    fields= "__all__"
    success_url = reverse_lazy('func_list')
