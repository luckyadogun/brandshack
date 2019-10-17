from django import forms

# ------- model imports -------- #
from .models import None


class TrialForm(forms.Form):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control memail', 'placeholder': 'john.doe@gmail.com'}))

class SignupForm(forms.ModelForm):
    pass