from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
import random
from .models import student

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

def dice(request):
    no = random.randint(1, 6)
    now = datetime.now()
    list1 = {"name": 'test', 'width': 28, 'height': 38}
    list2 = ['test2']
    return render(request, "dice.html", locals())

def search_student(request, id):
    try:
        student_id = student.objects.get(id=id)
    except:
        errormessage = r'讀取不存在或是錯誤!!'
    return render(request, "student.html", locals())



# Create your views here.
