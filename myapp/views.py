from django.shortcuts import render, redirect
from django.http import HttpResponse
from datetime import datetime
import random
from .models import student, comments
# from .models import *
from .form import django_form
from .upload import UploadFileForm

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


def articles(request):
    if request.method == 'GET':
        form = django_form()
        context = {"form":form}

    elif request.method == 'POST':
        d_form = django_form(request.POST)
        if d_form.is_valid():
            context = {
                "content":request.POST["content"],
                "email":request.POST["email"],
                "num":request.POST["num"],
            }
        else:
            context = {
                "errormsg": "錯誤的輸入值"
            }

    return render(request, "articles.html", locals())

def upload_file(request):
    if request.method == "POST":
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            print("form valid")
            file_name = str(request.POST['title']).strip('../').strip('./').strip('/')
            with open(f"./static/upload/{file_name}", 'wb+') as destination:
                for chunk in request.FILES['file']:
                    destination.write(chunk)
                return HttpResponse("File updated")
        else:
            print("form invalid")
    else:
        form = UploadFileForm()
        return render(request, "upload.html", {"form":form})
# Create your views here.
