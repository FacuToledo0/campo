from django.shortcuts import render, redirect
from .models import Campo
from .forms import ConsultaForm
from django.core.mail import send_mail
from django.conf import settings

def lista_campos(request):
    campos = Campo.objects.all()
    return render(request, 'propiedades/lista_campos.html', {'campos': campos})

def contacto(request):
    if request.method == 'POST':
        form = ConsultaForm(request.POST)
        if form.is_valid():
            consulta = form.save()  # Guarda la consulta en la base

            # 👉 ENVÍA EL CORREO
            send_mail(
                'Nueva consulta en Campos del Sur',
                f"Nombre: {consulta.nombre}\nEmail: {consulta.email}\nMensaje: {consulta.mensaje}",
                settings.DEFAULT_FROM_EMAIL,  # Remitente
                ['facundootoledo5@gmail.com'],      # A dónde querés recibirlo
                fail_silently=False,
            )

            return redirect('contacto')  # Redirige para evitar reenvíos
    else:
        form = ConsultaForm()

    return render(request, 'propiedades/contacto.html', {'form': form})

def nosotros(request):
    return render(request, 'propiedades/nosotros.html')

def inicio(request):
    return render(request, 'propiedades/inicio.html')


