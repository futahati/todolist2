# TodoList 專案

- 使用技術
    - Django 6.0.5

- 安裝套件
    - pip install django


## 專案結構

- manage.py

- settings.py(設定檔只有一個！)
    - ALLOWED_HOSTS = []
    - INSTALLED_APPS = []
    - ROOT_URLCONF = 'core.urls'
    - TEMPLATES = []
    - DATABASES = {}
    - LANGUAGE_CODE = 'en-us'
        - 修改 LANGUAGE_CODE = "zh-Hant"
    - TIME_ZONE = 'UTC'
        - 修改 TIME_ZONE = "Asia/Taipei"
    - USE_TZ = True
        - 修改 USE_TZ = False（上傳雲端時要改回來）

## 相關指令
- 新增專案（注意最後字元是「.」）
    - django-admin startproject core .

- 啟動server
    - python manage.py runserver

- 同步資料表
    - python manage.py makemigrations
        - 成功
            ```
            Migrations for 'todos':
            todos\migrations\0001_initial.py   
            + Create model Todo
            ```
    - python manage.py migrate
        - 成功
            ```
            Operations to perform:
            Apply all migrations: admin, auth, contenttypes, sessions, todos
            Running migrations:
            Applying todos.0001_initial... OK
            ```

- 建立管理員
    - python manage.py createsuperuser
        - 使用者名稱 (leave blank to use 'user'): irw
        - 電子郵件: futahati@gmail.com
        - Password: 
        - Password (again):
            - 這個密碼太常見了。
            - 這個密碼只包含數字。
            - Bypass password validation and create user anyway? [y/N]:y
        - Superuser created successfully.

- 新增APP
    - python manage.py startapp users
        - 修改 settings.py
            - 在 INSTALLED_APPS 新增→→ ["users",]
        - views.py（邏輯）
            - from django.http import HttpResponse
            - def index(request) →一定要寫(request)
        - 使用 core/urls.py（建立rater）
            - from users import views
            - urlpatterns = [path("admin/", admin.site.urls),path("", views.index),]


- 123
