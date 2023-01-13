from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html')

def demand(request):
    return render(request, 'demand.html')

def geography(request):
    return render(request, 'geography.html')

def skills(request):
    return render(request, 'skills.html')

def last_vacancies(request):
    return render(request, 'last-vacancies.html')