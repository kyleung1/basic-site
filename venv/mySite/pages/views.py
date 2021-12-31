from django.shortcuts import render
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect

# Create your views here.
def home_view(request, *args, **kwargs):
    return render(request, "home.html", {})

def resume_view(request, *args, **kwargs):
    return render(request, "resume.html", {})

def contact_view(request, *args, **kwargs):
    return render(request, "contact.html", {})

def about_view(request, *args, **kwargs):
    return render(request, "about.html", {})