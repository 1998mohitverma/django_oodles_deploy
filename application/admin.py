from django.contrib import admin
from .models import Student_table
# Register your models here.

@admin.register(Student_table)
class Student_admin(admin.ModelAdmin):
    list_display = ['id','name','email','contact','course','city','password']