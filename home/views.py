from django.shortcuts import render


def home(request):
    return render(request, 'home.html', {})


def about(request):
    return render(request, 'about.html', {})


def argali(request):
    return render(request, 'argali.html', {})


def argali_documentation(request):
    return render(request, 'argali-documentation.html', {})
