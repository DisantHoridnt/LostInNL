from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'website/index.html', {})

def about(request): 
    return render(request, 'website/about.html',)    

def contact(request):
    return render(request, 'website/contact.html',)

def listings(request):
    return render(request, 'website/listings.html',)

def resources(request):
    return render(request, 'website/resources.html',)

def submit(request):
    return render(request, 'website/submit.html',)
