from django.shortcuts import render, redirect
from django.http import HttpResponse
from datetime import datetime
import random
from .models import student, comments
# from .models import *

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

def redirect_test(request):
    return redirect('dice')

def posttest(request):
    return render(request, "posttest.html", locals())

def comment(request):
    if request.method == 'POST':
        message = request.POST['comment']
        #儲存進資料庫
        unit = comments.objects.create(comment_message=message)
        unit.save()
        return HttpResponse(message)


# Create your views here.
