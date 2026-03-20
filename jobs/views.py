from django.contrib import messages
from django.core.mail import send_mail
from django.shortcuts import redirect, render

from .forms import ApplicationForm


def apply_view(request):
    if request.method == "POST":
        form = ApplicationForm(request.POST)
        if form.is_valid():
            application = form.save()
            _notify_team(application)
            messages.success(
                request,
                "¡Gracias por postular! Tu información fue recibida correctamente.",
            )
            return redirect("jobs:apply")
    else:
        form = ApplicationForm()

    return render(request, "jobs/apply.html", {"form": form})


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
