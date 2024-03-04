from django.core.management.base import BaseCommand

class Command(BaseCommand):
    help = 'greetings'

    def add_arguments(self, parser):
        parser.add_argument('name' , type=str ,help='specifi name')

    def handle(self, *args, **kwargs):
        name=kwargs['name']
        greeting = f'hi {name} how are you' 
        self.stdout.write(self.style.SUCCESS(greeting))





