# Generated by Django 3.1.7 on 2021-05-11 17:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cuentas', '0002_cliente_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='telefono',
            field=models.BigIntegerField(blank=True, null=True),
        ),
    ]