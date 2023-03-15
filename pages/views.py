from django.shortcuts import render,redirect

def home(request):
    return render(request,template_name="pages/home.html")
