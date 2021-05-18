from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django import forms
from  django.contrib.auth.models import User

from .models import Pedido,Cliente

class ClienteForm(ModelForm):
    class Meta:
        model = Cliente
        fields = '__all__'
        exclude = ['user']

class PedidoForm(ModelForm):
    class Meta:
        model = Pedido
        #fields = ['cliente','videojuego']
        fields = '__all__'

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email','password1','password2']        