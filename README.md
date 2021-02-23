
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
STATIC_URL = '/static/'
STATICFILES_DIRS = [
    os.path.join.(BASE_DIR, 'static'),
]
###############################################################################
LANGUAGE_CODE = 'zh-Hant'

TIME_ZONE = 'Asia/Taipei'

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
```




