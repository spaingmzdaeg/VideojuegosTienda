# Generated by Django 3.1.7 on 2021-05-11 18:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cuentas', '0004_cliente_perfil_foto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='perfil_foto',
            field=models.ImageField(blank=True, null=True, upload_to='fotosperfil'),
        ),
    ]