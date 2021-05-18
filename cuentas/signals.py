from django.db.models.signals import post_save
#from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import Cliente
from django.contrib.auth.models import Group


def cliente_perfil(sender,instance,created,**kwargs):
    if created:
        group = Group.objects.get(name='clientes')
        instance.groups.add(group)

        Cliente.objects.create(
            user=instance,
            primer_nombre=instance.username,
            primer_apellido = instance.username,
        )
        print('perfil creado')

post_save.connect(cliente_perfil,sender=User)

