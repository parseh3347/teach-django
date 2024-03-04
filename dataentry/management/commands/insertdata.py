from dataentry.models import Student
from django.core.management.base import BaseCommand



class Command(BaseCommand):
    def handle(self,*args,**kwargs):

        dataset= [
            {'code':1001, 'username':'ali', 'email':'ali@gmail.com'},
            {'code':1002, 'username':'abas', 'email':'abas@gmail.com'},
            {'code':1005, 'username':'zx', 'email':'zx@gmail.com'},
        ]
        for data in dataset:
            code=data['code']
            record_exist = Student.objects.filter(code=code).exists()
            if not record_exist:
                Student.objects.create(code=data['code'], username=data['username'],email=data['email'])
            else:
                self.stdout.write(self.style.WARNING(f'data {code} is existed!'))

        self.stdout.write(self.style.SUCCESS(f'data { code } insert successfully!'))