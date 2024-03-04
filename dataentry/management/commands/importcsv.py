from django.core.management.base import BaseCommand
from dataentry.models import Student
from tkinter import filedialog
import csv

class Command(BaseCommand):
    help= ' import data file csv'

    # def add_arguments(self, parser) :
    #     parser.add_argument('file_path')
    
    def handle(self,*args, **kwargs):
        file_path= filedialog.askopenfilename()
        with open(file_path, 'r') as file:
            reader=csv.DictReader(file)
            for row in reader:
                code = row['code']
                record_exist = Student.objects.filter(code=code).exists()
                if not record_exist:
                    Student.objects.create(**row)
                    self.stdout.write(self.style.SUCCESS(f'add data {code} to database'))
                else:
                    self.stdout.write(self.style.WARNING(f'data {code} is exists'))