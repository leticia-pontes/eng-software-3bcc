import os
import sys
import django

# Set the Django settings module
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "termooo.settings")

# Add the project directory to the Python path
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)

# Initialize Django
django.setup()

from palavra.models import Palavra, Tema  # Import both models

# Get or create a theme instance (assuming you have a default theme)
default_tema, _ = Tema.objects.get_or_create(descricao='Geral')

with open('palavras.txt', 'r') as palavras_file:
    for palavra in palavras_file:
        p = Palavra()
        p.descricao = palavra.strip()  # Strip whitespace from the word
        p.tema_id = default_tema.id  # Set the tema_id field
        p.save()

# Retrieve all instances of the Palavra model and print them
all_palavras = Palavra.objects.all()
for palavra in all_palavras:
    print(palavra.descricao)
