from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request,"koru/index.html")

def host(request):
    return render(request,"koru/host.html")

def users(request):
    return render(request,"koru/users.html")