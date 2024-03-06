from django.core.management.base import BaseCommand
import csv
from dataentry.models import Student
from tkinter import filedialog
from datetime import datetime

class Command(BaseCommand):   
    help= 'data export to file csv'
    def handle(self,*args,**kwargs):
        students = Student.objects.all()

        timetamp = datetime.now().strftime('%Y-%m-%d-%H-%M-%S')
        filepath = f'export_data_to {timetamp}.csv'

        filetype=[('csv','*.csv'),('txt','*.txt',)]
        f=filedialog.asksaveasfilename(filetypes=filetype,defaultextension='.csv')

        with open(f,'w',newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['code','username','email'])

            for student in students:
                writer.writerow([student.code, student.username, student.email])

        self.stdout.write(self.style.SUCCESS('data export successfully!'))