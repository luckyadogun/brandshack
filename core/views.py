from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages

from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.core.mail import EmailMessage
# --------- forms imports -----------
from .forms import TrialForm, SignupForm

# --------- model imports -----------
from .models import User, AbandonedSignup, Customer
from .tokens import account_activation_token


# ---------- views ----------------

def index(request):
    if request.method == 'POST':
        trial_form = TrialForm(request.POST)
        if trial_form.is_valid():
            email = trial_form.cleaned_data['email']
            try:
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

    if tos and first_name and last_name and email and password and password2:
        if password == password2:
            # check if user was in abandoned signup and remove
            ab_user = AbandonedSignup.objects.filter(email=email_add)
            if ab_user.filter().exists():
                ab_user.delete()

            user = User.objects.create(
                first_name=first_name, 
                last_name=last_name,
                email=email_add,)
            user.set_password(password)
            user.is_active = False
            user.save()
            Customer.objects.create(user=user)
            # set activation link
            current_site = get_current_site(request)
            mail_subject = 'Activate your account'
            message = render_to_string('acc_active_email.html', {
                'user': "{} {}".format(user.first_name, user.last_name),
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)).decode(),
                'token': account_activation_token.make_token(user),
            })
            email = EmailMessage(mail_subject, message, to=[email_add])
            return activate_account(request, email=email_add)
        else:
            messages.error(request, "Passwords doesn't match. Try again!")
    return render(request, 'core/signup.html', {'email': email if email else ''})


def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        # login user
        # login(request, user)
        # redirect user to login with message of their active account
    else:
        # return user to activation page with message - activation link is invalid 

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

def activate_account(request, email=None):
    return render(request, 'core/activate_acct.html', {'email': email if email else ''})