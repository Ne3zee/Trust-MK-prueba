from django.views.generic import TemplateView, FormView
from django.urls import reverse_lazy
from django.contrib import messages
from jobs.forms import StitchApplicationForm

class HomeView(FormView):
    template_name = "core/stitch_landing.html"
    form_class = StitchApplicationForm
    success_url = reverse_lazy("core:home")

    def form_valid(self, form):
        form.save()
        messages.success(self.request, "¡Gracias por postular! Tu información fue recibida correctamente.")
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, "Hubo un error en tu postulación. Verifica que el CV sea PDF e intenta de nuevo.")
        return super().form_invalid(form)

class ServicesView(TemplateView):
    template_name = "core/services.html"

class AboutView(TemplateView):
    template_name = "core/about.html"

class ContactView(TemplateView):
    template_name = "core/contact.html"