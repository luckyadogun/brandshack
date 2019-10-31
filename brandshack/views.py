from django.shortcuts import render

def handler404(request, exception):
    return render(request, 'core/404.html', {})

def handler500(request):
    return render(request, 'core/500.html', {})