from django.shortcuts import render
from django.contrib.auth import logout

# Create your views here.
def index(request):
    return render(request,'index.html')

def home(request):
    return render(request,'home.html')

def userlogout(request):
    logout(request)
    return render(request,'index.html')