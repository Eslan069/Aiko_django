from django.shortcuts import render
from .models import AllUsers

def cadastro(request):
    if request.method == "GET":
        return render(request, 'cadastro.html')
    elif request.method == "POST":
        email = request.POST.get('email')
        senhe = request.POST.get('senhe')
        print(email)
        return render(request, 'cadastro.html')

def login(request):
    return render(request, 'login.html')
