from django.contrib import admin
from myapp.models import student, comments

# Register your models here.

# admin.site.register(student)


class studentAdmin(admin.ModelAdmin):
    list_display=('id', 'cName', 'cBirthday', 'cEmail', 'cPhone', 'cAddr')
    #資料過濾
    list_filter = ('cName', 'cSex')
    #依欄位搜尋
    search_fields = ('cName', )
    #按照id來排序
    ordering = ('id', )

admin.site.register(student, studentAdmin)
admin.site.register(comments)
