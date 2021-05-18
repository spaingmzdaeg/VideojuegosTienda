from django.urls import path
from . import views
from .views import accountSettings, render_pdf_view,PedidosListView,pedidos_render_pdf_view


urlpatterns = [
    path('register/', views.registerPage, name="register"),
    path('login/', views.loginPage, name="login"),
    path('logout/', views.logoutUser, name="logout"),
    path('user/',views.userPage,name='user-page'),
    path('account/',views.accountSettings,name="account"),

    path('', views.home,name="home"),
    path('videojuegos/',views.videojuegos,name='videojuegos'),
    path('cliente/<str:pk_test>/',views.cliente,name='cliente'),
    path('clientes/',views.clientes,name='clientes'),
    path('pedidos/',views.pedidos,name='pedidos'),
    path('crear_pedido/<str:pk>',views.crearPedido,name='crear_pedido'),
    path('actualizar_pedido/<str:pk>',views.actualizarPedido,name='actualizar_pedido'),
    path('eliminar_pedido/<str:pk>',views.eliminarPedido,name='eliminar_pedido'),
    path('crear_pedido_tabla',views.crearPedidoTablaPedidos,name='crear_pedido_tabla'),
    path('pedidos-list-view',views.PedidosListView.as_view(),name='pedidos-list-view'),
    path('test/',views.render_pdf_view,name='test-view'),
    path('pdf/<pk>/',views.pedidos_render_pdf_view,name='pedido-pdf-view'),
    path('pie-chart/', views.pie_chart, name='pie-chart'),
]

