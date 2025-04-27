from django.shortcuts import render

# Create your views here.
def aboutus(request):
    return render(request, 'about/abouths.html')

def contract(request):
    return render(request, 'about/contact.html')

def developers(request):
    return render(request, 'about/dev.html')