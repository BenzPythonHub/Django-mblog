
# 網站上線後將settings中的DEBUG 改為False才不會早成資安風險

####  安裝 Django
```bash
python -m pip install django
```

#### 安裝相關套件
```bash
python -m pip install -r requirements.txt
```

#### 啟動django專案
```bash
django-admin startproject <project_name>
```

#### 進入專案
```bash
cd <project_name>
```

#### 創建app
```bash
python manage.py startapp <app_name>
```

#### 到 settings.py中 找到 INSTALLED_APPS 加入
```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    '<app_name>',
]
```

#### 建立templates && static 目錄
```bash
sudo mkdir templates
sudo mkdir static
```

#### 設定database為mysql 到 settings.py中 找到database
```python
DATABASES = {
    'default': {
        # 'ENGINE': 'django.db.backends.sqlite3',
        # 'NAME': BASE_DIR / 'db.sqlite3',

        'ENGINE': 'django.db.backends.mysql',  
        'NAME': '<database_name>',                
        'USER': '<user_name>',                        
        'PASSWORD': '<password>',                  
        'HOST': '<your_mysql_IP>', #defaul 127.0.0.1 or localhost                
        'PORT': '3306',   #mysql's default 3306                     
    }
}
```

#### 在與settings.py同一層目錄的__init__.py中加入pymysql套件
```python
import pymysql
pymysql.install_as_MySQLdb()
```

#### 建立migration(初次的情況下)
```bash
python manage.py makemigrations
python manage.py migrate
```

#### 啟動django 預設開發網頁伺服器
```bash
python manage.py runserver
```

####  在settings.py中 設定templates && static目錄路徑 和更改語系和時區
```bash
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        #這邊修改
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]
###############################################################################
STATIC_ROOT = 'staticfiles'
STATIC_URL = '/static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
]
###############################################################################
LANGUAGE_CODE = 'zh-Hant'

TIME_ZONE = 'Asia/Taipei'

```

#### gunicorn 佈署後css .js無法讀取問題
```bash
#All You need is dj-static package.
python -m pip install dj-static
#Configure your static assets in settings.py:
STATIC_ROOT = 'staticfiles'
STATIC_URL = '/static/'
#Then, update your wsgi.py file to use dj-static:
from django.core.wsgi import get_wsgi_application
from dj_static import Cling

application = Cling(get_wsgi_application())
```

#### render 語法
```python
#第一個參數是HttpRequest物件,第二個參數是模板名稱,最後一個參數是字典
render(request, template_name, context)
#例如,傳遞字典{"no":1, "name": "Amy", "age": 20}給顯示模板dice.html
dict1 = {"no":1, "name": "Amy", "age": 20}
render(request, "dice.html", dict1)
```

#### template 語言
```python
#判斷式
{% if score >= 90 %}
    your_pass = 'good'
{% elif score >= 60 %}
    your_pass = True
{% else %}
    your_pass = False
{% endif %}
#迴圈
{% for i in list1 %}
    {{ i }},
{% empty %}
    沒有資料
{% endfor %}

#繼承模板
{% extends "base_header.html" %}
#主內容區
{% block content %}
    <h1>Hi, This is me ~</h1>
{% endblock %}

#側邊欄位
{% block sidebar %}
    <ul class="sidebar-nav">
{% endblock %}
{% extends "base_footer.html" %}
```

#### 在model.py中定義class類別,每一個類別相當一個表

#### 利用admin可以管理後台,新增.修改或刪除資料,在Admin管理界面中可以設定顯示多個欄位資料

#### 創建後台使用者帳號密碼
```python
python manage.py createsuperuser
```

#### Django ORM CRUD
```python
#資料庫欄位資料屬性
#創立ID用
AutoField:id models.AutoField(primary_key=True)
#日期
DateField
DateTimeField
#數字
IntegerField
#內容
CharField
TextField
#網站
URLField
#UUID
UUIDField
#Email
EmailField
#檔案
FileField
#圖片
ImageField

#Django QuerySet API
from myapp.models import student
#create
student.objects.create(cName='王大明', cSex='M', cBirthday='1977-09-28', cEmail='wangming@gmail.com', cPhone='0911123456', cAddr='台北市羅斯福路一段3號')
#read
student.objects.all()
#單筆資料查尋
student.objects.get(pk=1)
student.objects.filter(cName='李大大')
#廣泛查詢 這裡使用 contains 針對cName欄位，篩選出所有標題中包含李字眼的 student
student.objects.filter(cName__contains='李')

#update
student_lee = student.objects.filter(cName__contains='李')
student_lee[0]
student_lee[1]
student_lee.update(cName='李冰冰')

#delete
student_lee.delete()

```

#### views 裝飾子
```python
#需要登入才能使用此函式
@method_decorator(login_required)
#永遠不要有cache
@never_cache(view_func)
#規定請求的方法
@require_http_methods(["GET", "POST"])
```




