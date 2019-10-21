from django import forms

# ------- model imports -------- #


class TrialForm(forms.Form):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control memail', 'placeholder': 'john.doe@gmail.com'}))

