
from django.shortcuts import render, redirect, get_object_or_404
from .models import Restaurante, Plato

def restaurante_list(request):
    """Lista todos los restaurantes."""
    restaurantes = Restaurante.objects.all()
    return render(request, 'restaurante/restaurante_list.html', {'restaurantes': restaurantes})

def restaurante_create(request):
    """Crea un nuevo restaurante con formulario manual."""
    if request.method == 'POST':
        
        nombre = request.POST.get('nombre')
        direccion = request.POST.get('direccion')
        horario = request.POST.get('horario_apertura')
        telefono = request.POST.get('telefono')
        logo_file = request.FILES.get('logo')

        Restaurante.objects.create(
            nombre=nombre,
            direccion=direccion,
            horario_apertura=horario,
            telefono=telefono,
            logo=logo_file 
        )
        return redirect('restaurante_list')
    #si es get
    return render(request, 'restaurante/restaurante_form.html', {'action': 'Crear'})

def restaurante_update(request, pk):
    restaurante = get_object_or_404(Restaurante, pk=pk)
    if request.method == 'POST':
        restaurante.nombre = request.POST.get('nombre')
        restaurante.direccion = request.POST.get('direccion')
        restaurante.horario_apertura = request.POST.get('horario_apertura')
        restaurante.telefono = request.POST.get('telefono')
        if request.FILES.get('logo'):
            restaurante.logo = request.FILES.get('logo')
            
        restaurante.save()
        return redirect('restaurante_list')
    return render(request, 'restaurante/restaurante_form.html', {'restaurante': restaurante, 'action': 'Editar'})

def restaurante_delete(request, pk):
    """Elimina un restaurante."""
    restaurante = get_object_or_404(Restaurante, pk=pk)
    if request.method == 'POST':
        restaurante.delete()
        return redirect('restaurante_list')
    return render(request, 'restaurante/restaurante_confirm_delete.html', {'restaurante': restaurante})



# vistas para modelo plato 
def plato_list(request):
    platos = Plato.objects.all().select_related('restaurante')
    return render(request, 'restaurante/plato_list.html', {'platos': platos})

def plato_create(request):
    restaurantes = Restaurante.objects.all() 

    if request.method == 'POST':
        restaurante_id = request.POST.get('restaurante')
        nombre = request.POST.get('nombre')
        descripcion = request.POST.get('descripcion')
        precio = request.POST.get('precio')
        tipo_comida = request.POST.get('tipo_comida')
        foto_file = request.FILES.get('foto') 
        restaurante_instance = get_object_or_404(Restaurante, pk=restaurante_id)
        Plato.objects.create(
            restaurante=restaurante_instance,
            nombre=nombre,
            descripcion=descripcion,
            precio=precio,
            tipo_comida=tipo_comida,
            foto=foto_file
        )
        return redirect('plato_list')

    return render(request, 'restaurante/plato_form.html', {'restaurantes': restaurantes, 'action': 'Crear'})

def plato_update(request, pk):
    plato = get_object_or_404(Plato, pk=pk)
    restaurantes = Restaurante.objects.all() 
    
    if request.method == 'POST':
        restaurante_id = request.POST.get('restaurante')
        restaurante_instance = get_object_or_404(Restaurante, pk=restaurante_id)
        plato.restaurante = restaurante_instance
        plato.nombre = request.POST.get('nombre')
        plato.descripcion = request.POST.get('descripcion')
        plato.precio = request.POST.get('precio')
        plato.tipo_comida = request.POST.get('tipo_comida')
        if request.FILES.get('foto'):
            plato.foto = request.FILES.get('foto')
            
        plato.save()
        return redirect('plato_list')

    context = {
        'plato': plato, 
        'restaurantes': restaurantes, 
        'action': 'Editar'
    }
    return render(request, 'restaurante/plato_form.html', context)

def plato_delete(request, pk):
    plato = get_object_or_404(Plato, pk=pk)
    if request.method == 'POST':
        plato.delete()
        return redirect('plato_list')    
    return render(request, 'restaurante/plato_confirm_delete.html', {'plato': plato})