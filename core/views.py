from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages
from django.utils.encoding import force_text
from django.utils.http import urlsafe_base64_decode
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

# --------- forms imports -----------
from .forms import TrialForm

# --------- model imports -----------
from .models import User, AbandonedSignup, Customer
from .tokens import account_activation_token
from .helpers import _email_activate_acct, _email_design_request, generate_customer_id


# ---------- views ----------------
def index(request):
    if request.method == 'POST':
        trial_form = TrialForm(request.POST)
        if trial_form.is_valid():
            email = trial_form.cleaned_data['email']
            try:
                #TODO:
                # add user to a newsletter for reminders
                # notify admin
                AbandonedSignup.objects.create(email=email)
            except:
                pass
            return signup(request, email=email)
    else:
        trial_form = TrialForm()
    return render(request, 'core/index.html', {'trial_form': trial_form})


def signup(request, email=None):
    tos = request.POST.get('tos')
    first_name = request.POST.get('f_name')
    last_name = request.POST.get('l_name')
    email_add = request.POST.get('email')
    password = request.POST.get('password')
    password2 = request.POST.get('password2')

    if tos:
        if password == password2:
            # check if user was in abandoned signup and remove
            ab_user = AbandonedSignup.objects.filter(email=email_add)
            if ab_user.filter().exists():
                ab_user.delete()

            try:
                user = User.objects.create(
                    first_name=first_name, 
                    last_name=last_name,
                    email=email_add,)
                user.set_password(password)
                user.is_active = False
                user.save()
                Customer.objects.create(user=user, customer_id=generate_customer_id())

                # send activation link
                _email_activate_acct(request, user_pk=user.pk)
                return activate_account(request, email=email_add)
            except:
                # user already has an account
                messages.error(request, "You already have an account! Try logging in.")
                return redirect('/login/')

        else:
            messages.error(request, "Passwords doesn't match. Try again!")
    return render(request, 'core/signup.html', {'email': email if email else ''})


def activate_account(request, email=None):
    "view function to handle notify user of activation link"
    return render(request, 'core/activate_acct.html', {'email': email if email else ''})

def activate(request, uidb64, token):
    "a view function to activate account"
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        messages.error(request, "You account is active! Log in")
        return redirect('/login/')
    else:
       return redirect('/activate-account/')

def login_user(request):
    email_add = request.POST.get('email')
    password = request.POST.get('password')
    if email_add and password:
        user = authenticate(email=email_add, password=password)
        if user is not None:
            login(request, user)
            return redirect('/dashboard/')
        else:
            messages.error(request, "account does not exist")
            return redirect('/login/')
    return render(request, 'core/login.html', {})

@login_required
def dashboard(request):
    customer = get_object_or_404(Customer, user=request.user.id)
    platform = request.POST.get('platform')
    brief = request.POST.get('brief')
    _email_design_request(customer=customer, platform=platform, brief=brief)
    messages.success(request, "Your request has been sent!")
    return render(request, 'core/dashboard.html', {})

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

def logout_user(request):
    logout(request)
    return index(request)