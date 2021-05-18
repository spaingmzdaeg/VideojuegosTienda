import django_filters
from django_filters import DateFilter,CharFilter

from .models import Videojuego,Cliente,Tag,Pedido

class PedidoFilter(django_filters.FilterSet):
    fecha_inicio = DateFilter(field_name="fecha_pedido",lookup_expr='gte')
    fecha_final = DateFilter(field_name="fecha_pedido",lookup_expr='lte')
    nota =  CharFilter(field_name='nota', lookup_expr='icontains')
    videojuego_nombre =  CharFilter(field_name='videojuego__nombre', lookup_expr='icontains')
    
    class Meta:
        model = Pedido
        fields = '__all__'
        exclude = ['cliente','fecha_pedido','videojuego_nombre']

class PedidoFilterTablaPedidos(django_filters.FilterSet):
    class Meta:
        model = Pedido
        fields = '__all__'
