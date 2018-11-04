from django.shortcuts import render, redirect
from django.http import HttpResponse
from apps.producto.forms import ProductoForm
from apps.producto.models import Producto
# Create your views here.


def index(request):
    return render(request, 'producto/producto.html')

def producto_view(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('producto:index')
    else:
        form = ProductoForm()
        
    return render(request, 'producto/producto_form.html', {'form':form})

def producto_list(request):
    producto = Producto.objects.all()
    contexto = {'productos':producto}
    return render(request, 'producto/producto_list.html', contexto)

def producto_edit(request, id_producto):
    producto = Producto.objects.get(id=id_producto)
    if request.method == 'GET':
        form = ProductoForm(instance=producto)
    else:
        form = ProductoForm(request.POST, instance=producto)
        if form.is_valid():
            form.save()
        return redirect('producto:producto_listar')
    return render(request, 'producto/producto_form.html', {'form':form})

def producto_delete(request, id_producto):
    producto = Producto.objects.get(id=id_producto)
    if request.method == 'POST':
        producto.delete()
        return redirect('producto:producto_listar')
    return render(request, 'producto/producto_delete.html', {'producto':producto})