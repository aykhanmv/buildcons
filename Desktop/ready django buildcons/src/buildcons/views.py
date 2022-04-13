
from django.shortcuts import render

def home(request):
    return render(request, 'index.html', {'title': 'Elşənoğlu inşaat'})

def about(request):
    return render(request, 'readmore.html', {'title': 'Elşənoğlu inşaat'})

def contact(request):
    return render(request, 'contactus.html', {'title': 'Elşənoğlu inşaat'})

def interdesign(request):
    return render(request, 'interdesign.html', {'title': 'Elşənoğlu inşaat'})

def building(request):
    return render(request, 'building.html', {'title': 'Elşənoğlu inşaat'})

def renovation(request):
    return render(request, 'renovation.html', {'title': 'Elşənoğlu inşaat'})

def exdesign(request):
    return render(request, 'exdesign.html', {'title': 'Elşənoğlu inşaat'})

def projection(request):
    return render(request, 'projection.html', {'title': 'Elşənoğlu inşaat'})