from django.urls import path

from .views import AboutView, ContactView, ServicesView, home_view

app_name = "core"

urlpatterns = [
    path("", home_view, name="home"),
    path("servicios/", ServicesView.as_view(), name="services"),
    path("quienes-somos/", AboutView.as_view(), name="about"),
    path("contacto/", ContactView.as_view(), name="contact"),
]
