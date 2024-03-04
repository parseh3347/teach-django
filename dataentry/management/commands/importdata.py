from django.core.management.base import BaseCommand, CommandParser
import shutil
from tkinter import filedialog

class Command(BaseCommand):   
    def handle(self,*args,**kwargs):
        # filepath=filedialog.askopenfilename()
        with open('Desktop\w.txt','r') as p :
            # a=p.readlines()
            with open('Desktop\ww.txt','ta') as pp:
            # b=pp.readlines()
                shutil.copyfileobj(p,pp)
            if len(p)==0:
                self.stdout.write(self.style.SUCCESS('successfully!'))