from django.contrib import admin
from .models import student, info
# Register your models here.

@admin.register(student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['id', 'roll', 'name', 'course']

@admin.register(info)
class InfoData(admin.ModelAdmin):
    list_display = ['id', 'name', 'email', 'number' ,'course']