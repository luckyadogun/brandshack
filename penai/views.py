from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def name_gen(request):
    return render(request, 'penai/namegen.html', {})