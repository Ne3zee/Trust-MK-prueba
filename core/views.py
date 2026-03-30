from django.shortcuts import render
from django.views.generic import TemplateView


def home_view(request):
    return render(request, "core/landing.html")


class ServicesView(TemplateView):
    template_name = "core/services.html"


class AboutView(TemplateView):
    template_name = "core/about.html"


class ContactView(TemplateView):
    template_name = "core/contact.html"
