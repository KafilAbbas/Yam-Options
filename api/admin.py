from django.contrib import admin
from .models import *
@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['id','stuname','email']
# Register your models here.
admin.site.register(DataFrameStorage)