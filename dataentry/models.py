from django.db import models

# Create your models here.

class Student(models.Model):
    code = models.PositiveIntegerField(unique=True,verbose_name='کد')
    username = models.CharField(max_length = 150, verbose_name='نام کاربری')
    email = models.EmailField(max_length=254, unique=True , verbose_name='ایمیل')
    

    def __str__(self) -> str:
        return self.username