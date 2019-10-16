from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, 'core/index.html', {})

def how_it_works(request):
    return render(request, 'core/how-it-works.html', {})

def samples(request):
    return render(request, 'core/samples.html', {})

def pricing(request):
    return render(request, 'core/pricing.html', {})