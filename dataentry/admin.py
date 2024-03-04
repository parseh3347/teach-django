from django.contrib import admin
from dataentry.models import Student

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = [
        'code',
        'username',
        'email',
    ]