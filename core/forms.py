from django import forms

# ------- model imports -------- #


class TrialForm(forms.Form):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control memail', 'placeholder': 'john.doe@gmail.com'}))

class SignupForm(forms.Form):
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'text_box', 'placeholder': 'First Name'}))
