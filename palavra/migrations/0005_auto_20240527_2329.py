from django.db import migrations
from django.contrib.auth.hashers import make_password

def set_default_password(apps, schema_editor):
    Cadastro = apps.get_model('palavra', 'Cadastro')
    for cadastro in Cadastro.objects.all():
        cadastro.senha = make_password('temp')
        cadastro.save()

class Migration(migrations.Migration):

    dependencies = [
        ('palavra', '0004_cadastro_senha'),
    ]

    operations = [
        migrations.RunPython(set_default_password),
    ]
