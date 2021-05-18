# Generated by Django 3.1.7 on 2021-05-11 19:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('cuentas', '0005_auto_20210511_1842'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='perfil_foto',
            field=models.ImageField(blank=True, default='user.png', null=True, upload_to='fotosperfil'),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='user',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
