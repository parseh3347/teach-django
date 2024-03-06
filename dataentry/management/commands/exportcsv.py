from django.core.management.base import BaseCommand
import csv
from dataentry.models import Student
from tkinter import filedialog
from datetime import datetime

class Command(BaseCommand):   
    help= 'data export to file csv'

    students= Student.objects.all()

    def handle(self,*args,**kwargs):
        timemap=datetime.now().strftime('%Y-%m-%d-%H-%M-%S')
        datefile=f'{timemap}'

        typefile = [('csv','*.csv'),('txt','*.txt')]
        f=filedialog.asksaveasfilename(filetypes=typefile,defaultextension='.csv')

        with open(f,'ta',newline='') as file:
            writer=csv.writer(file)
            writer.writerow(['serial_number','name','emil','date'])

            for student in self.students:
                writer.writerow([student.code,student.username,student.email,datefile])
        
        self.stdout.write(self.style.SUCCESS('data export sucessfully'))