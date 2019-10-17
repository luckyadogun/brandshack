from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect

# --------- forms imports -----------
from .forms import TrialForm, SignupForm

# --------- model imports -----------
from .models import AbandonedSignup



# ---------- views ----------------

def index(request):
    if request.method == 'POST':
        trial_form = TrialForm(request.POST)
        if trial_form.is_valid():
            email = trial_form.cleaned_data['email']
            return signup(request, email=email)
    else:
        trial_form = TrialForm()
    return render(request, 'core/index.html', {'trial_form': trial_form})


def signup(request, email=None):
    tos = request.POST.get('tos')
    first_name = request.POST.get('f_name')
    last_name = request.POST.get('l_name')
    email = request.POST.get('email')
    password = request.POST.get('password')

    if tos and first_name and last_name and email and password:
        # register user and make account inactive
        print("wowwy")
        pass
    return render(request, 'core/signup.html', {'email': email if email else ''})



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

def login(request):
    return render(request, 'core/login.html', {})