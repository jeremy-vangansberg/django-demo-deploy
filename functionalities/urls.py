from django.urls import path

from . import views

urlpatterns = [
    path('', views.FunctionalitiesListView.as_view(), name='func_list'),
    path('functionalities_create/', views.FunctionalitiesCreateView.as_view(), name='func_create'),
    path('functionalities_detail/<int:pk>', views.FunctionalitiesDetailView.as_view(), name='func_detail')
]
