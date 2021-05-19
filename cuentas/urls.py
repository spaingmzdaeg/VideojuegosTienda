from django.urls import path
from django.contrib.auth import views as auth_views
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

    path('reset_password/',
     auth_views.PasswordResetView.as_view(template_name="cuentas/password_reset.html"),
     name="reset_password"),

    path('reset_password_sent/', 
        auth_views.PasswordResetDoneView.as_view(template_name="cuentas/password_reset_sent.html"), 
        name="password_reset_done"),

    path('reset/<uidb64>/<token>/',
     auth_views.PasswordResetConfirmView.as_view(template_name="cuentas/password_reset_form.html"), 
     name="password_reset_confirm"),

    path('reset_password_complete/', 
        auth_views.PasswordResetCompleteView.as_view(template_name="cuentas/password_reset_done.html"), 
        name="password_reset_complete"),

]

