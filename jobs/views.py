from django.contrib import messages
from django.core.mail import send_mail
from django.shortcuts import redirect, render
from .models import postulaciones

from .forms import ApplicationForm


def apply_view(request):
    if request.method == "POST":
        form = ApplicationForm(request.POST)
        if form.is_valid():
            application = form.save()
            
            # Guardamos explícitamente en la tabla manual 'postulaciones'
            try:
                postulaciones.objects.create(
                    nombre_completo=application.full_name,
                    telefono=application.phone,
                    email=application.email,
                    edad=application.age,
                    experiencia_ventas=application.get_sales_experience_display(),
                    disponibilidad=application.availability,
                    comentarios=application.additional_comments
                )
            except Exception as e:
                print(f"Error guardando en la tabla manual postulaciones: {e}")

            _notify_team(application)
            messages.success(
                request,
                "¡Gracias por postular! Tu información fue recibida correctamente.",
            )
            return redirect("core:home")
        else:
            # Si el formulario no es válido, redirigir a home con mensaje de error
            messages.error(
                request,
                "Hubo un error en tu postulación. Por favor revisa los datos e intenta de nuevo.",
            )
            return redirect("core:home")
    
    # GET requests a /jobs/ redirigen al home
    return redirect("core:home")


def _notify_team(application):
    send_mail(
        subject=f"Nueva postulación: {application.full_name}",
        message=(
            "Se recibió una nueva postulación en TrustMarket.\n\n"
            f"Nombre: {application.full_name}\n"
            f"Teléfono: {application.phone}\n"
            f"Correo: {application.email}\n"
            f"Edad: {application.age}\n"
            f"Experiencia: {application.get_sales_experience_display()}\n"
            f"Disponibilidad: {application.availability}\n"
        ),
        from_email=None,
        recipient_list=["reclutamiento@trustmarket.cl"],
        fail_silently=True,
    )