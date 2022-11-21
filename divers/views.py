from django.shortcuts import render

# Create your views here.
def home_page(request):
    return render(request, 'divers/home_page.html')