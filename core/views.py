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

def team(request):
    return render(request, 'core/team.html', {})

def faq(request):
    return render(request, 'core/faq.html', {})

def contact(request):
    return render(request, 'core/contact.html', {})

def signup(request):
    return render(request, 'core/signup.html', {})

def login(request):
    return render(request, 'core/login.html', {})