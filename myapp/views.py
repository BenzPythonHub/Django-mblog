from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime

def sayhello(request):
    return HttpResponse("Hello Django XD")

def sayuserhello(request, username):
    return HttpResponse(f"Hello {username}")

def hellotemplate(request, username):
    now = datetime.now()
    return render(request, "hellotemplate.html", locals())

def hellofulltemplate(request, username):
    now = datetime.now()
    return render(request, "hellofulltemplate.html", locals())

# Create your views here.
