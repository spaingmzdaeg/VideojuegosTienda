from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from django.forms import inlineformset_factory
from .models import Videojuego,Cliente,Tag,Pedido
from .forms import ClienteForm, PedidoForm,CreateUserForm
from .filters import PedidoFilter,PedidoFilterTablaPedidos
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger

from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa
from django.views.generic import ListView

from django.db.models import Count
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
from .decorators import unauthenticated_user,allowed_users,admin_only
# Create your views here.

@unauthenticated_user
def registerPage(request):  
        form = CreateUserForm()
        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                user = form.save()
                username = form.cleaned_data.get('username')
                

                messages.success(request, 'Account was created for ' + username )

                return redirect('login')

        context = {'form':form}
        return render(request, 'cuentas/register.html', context)

@unauthenticated_user
def loginPage(request):
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request,username=username,password=password)

            if user is not None:
                login(request,user)
                return redirect('home')
            else:
                messages.info(request,'Username OR password incorrect')

        context = {}
        return render(request, 'cuentas/login.html', context)

def logoutUser(request):
    logout(request)
    return redirect('login')

     
@login_required(login_url='login')
@admin_only
def home(request):
    pedidos = Pedido.objects.all()
    clientes = Cliente.objects.all()

    clientesTotales = clientes.count()

    pedidosTotales = pedidos.count()

    pedidosEntregados = pedidos.filter(estatus='ENTREGADO').count()

    pedidosNoDisponibles = pedidos.filter(estatus='NO DISPONIBLE').count()

    pedidosPendientes = pedidos.filter(estatus='PENDIENTE').count()

    page = request.GET.get('page',1)
    paginator = Paginator(pedidos,4)

    try:
        listaPedidos = paginator.page(page)
    except PageNotAnInteger:
        listaPedidos = paginator.page(1)
    except EmptyPage:
        listaPedidos = paginator.page(paginator.num_pages)

    context = {'pedidos':pedidos,'clientes':clientes,'pedidosTotales':
    pedidosTotales,'pedidosEntregados':pedidosEntregados,
    'pedidosPendientes':pedidosPendientes,'listaPedidos':listaPedidos}

    return render(request,'cuentas/dashboard.html',context)

@login_required
@allowed_users(allowed_roles=['admin','clientes'])
def userPage(request):
    pedidos = request.user.cliente.pedido_set.all()
    pedidosTotales = pedidos.count()

    pedidosEntregados = pedidos.filter(estatus='ENTREGADO').count()

    pedidosNoDisponibles = pedidos.filter(estatus='NO DISPONIBLE').count()

    pedidosPendientes = pedidos.filter(estatus='PENDIENTE').count()

    #print('PEDIDOS:',pedidos)
    context = {'pedidos':pedidos,'pedidosTotales':
    pedidosTotales,'pedidosEntregados':pedidosEntregados,
    'pedidosPendientes':pedidosPendientes}
    return render(request, 'cuentas/user.html', context)

@login_required
@allowed_users(allowed_roles=['admin','clientes'])
def accountSettings(request):
    cliente = request.user.cliente
    form = ClienteForm(instance=cliente)
    
    if request.method == 'POST':
        form = ClienteForm(request.POST,request.FILES,instance=cliente)
        if form.is_valid():
            form.save()

    context  = {'form':form}
    return render(request, 'cuentas/account_settings.html', context)    

@login_required(login_url='login')
def videojuegos(request):
    videojuegos = Videojuego.objects.all()
    return render(request,'cuentas/videojuegos.html',{'videojuegos':videojuegos})

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def cliente(request,pk_test):
    cliente = Cliente.objects.get(id=pk_test)
    pedidos = cliente.pedido_set.all()
    cantidadPedidos = pedidos.count()
    myFilter = PedidoFilter(request.GET,queryset=pedidos)
    pedidos = myFilter.qs
    context = {'cliente':cliente,'pedidos':pedidos,'cantidadPedidos':
    cantidadPedidos,'myFilter':myFilter}
    return render(request,'cuentas/cliente.html',context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def clientes(request):
    clientes = Cliente.objects.all()
    return render(request,'cuentas/clientes.html',{'clientes':clientes})

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def pedidos(request):
    pedidos = Pedido.objects.all()
    myFilter = PedidoFilterTablaPedidos(request.GET,queryset=pedidos)
    pedidos = myFilter.qs
    page = request.GET.get('page',1)
    paginator = Paginator(pedidos,4)

    try:
        listaPedidos = paginator.page(page)
    except PageNotAnInteger:
        listaPedidos = paginator.page(1)
    except EmptyPage:
        listaPedidos = paginator.page(paginator.num_pages)



    context = {'pedidos':pedidos,'myFilter':myFilter,'listaPedidos':listaPedidos}
    return render(request,'cuentas/pedidos.html',context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def crearPedido(request,pk):
    PedidoFormSet = inlineformset_factory(Cliente,Pedido,fields=('videojuego','estatus'),extra=10)
    cliente = Cliente.objects.get(id=pk)
    formset = PedidoFormSet(queryset=Pedido.objects.none(),instance=cliente)
    #form = PedidoForm(initial={'cliente':cliente})
    if request.method == 'POST':
        #print('Post Impreso:',request.POST)
        formset = PedidoFormSet(request.POST,instance=cliente)
        if formset.is_valid():
            formset.save()
            return redirect('/pedidos')            
    context = {'form':formset}
    return render(request,'cuentas/formulario_pedidos.html',context)    

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def crearPedidoTablaPedidos(request):
    form = PedidoForm()
    if request.method == 'POST':
        form = PedidoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/pedidos')
    context = {'form':form}
    return render(request,'cuentas/formulario_pedidos_tabla.html',context)   

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def actualizarPedido(request , pk):
    pedido = Pedido.objects.get(id=pk)
    form = PedidoForm(instance=pedido)
    if request.method == 'POST':
        #print('Post Impreso:',request.POST)
        form = PedidoForm(request.POST,instance=pedido)
        if form.is_valid():
            form.save()
            return redirect('/pedidos')
    context = {'form':form}
    return render(request,'cuentas/formulario_pedidos.html',context) 

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def eliminarPedido(request,pk):
    pedido = Pedido.objects.get(id=pk)
    if request.method == "POST":
        pedido.delete()
        return redirect('/pedidos')
    context = {'item':pedido}
    return render(request,'cuentas/eliminar.html',context)    


class PedidosListView(ListView):
    model = Pedido
    template_name = 'cuentas/reporte_pedidos_template.html'

#vistas reportes
@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def pedidos_render_pdf_view(request,*args, **kwargs):
    pk = kwargs.get('pk')
    pedido = get_object_or_404(Pedido,pk=pk)

    template_path = 'cuentas/pdf2.html'
    context = {'pedido': pedido}
    # Create a Django response object, and specify content_type as pdf
    response = HttpResponse(content_type='application/pdf')
    # if download:
    #response['Content-Disposition'] = 'attachment; filename="report.pdf"'
    # find the template and render it.
    #if display:
    response['Content-Disposition'] = 'filename="report.pdf"'
    template = get_template(template_path)
    html = template.render(context)

    # create a pdf
    pisa_status = pisa.CreatePDF(
       html, dest=response)
    # if error then show some funy view
    if pisa_status.err:
       return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response




@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def render_pdf_view(request):
    template_path = 'cuentas/pdf1.html'
    context = {'myvar': 'this is your template context'}
    # Create a Django response object, and specify content_type as pdf
    response = HttpResponse(content_type='application/pdf')
    # if download:
    #response['Content-Disposition'] = 'attachment; filename="report.pdf"'
    # find the template and render it.
    #if display:
    response['Content-Disposition'] = 'filename="report.pdf"'
    template = get_template(template_path)
    html = template.render(context)

    # create a pdf
    pisa_status = pisa.CreatePDF(
       html, dest=response)
    # if error then show some funy view
    if pisa_status.err:
       return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response

#vistas para graficas
@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def pie_chart(request):
    labels = []
    data = []
    pedidos = Pedido.objects.all()
    queryset = Pedido.objects.order_by('estatus').values('estatus').annotate(estatus_count=Count('estatus'))
    data = list(queryset.values_list('estatus_count', flat=True))
    labels = list(queryset.values_list('estatus', flat=True))


    return render(request,'cuentas/pie_chart.html', {
        'labels':labels,
        'data':data,
    })    
    
