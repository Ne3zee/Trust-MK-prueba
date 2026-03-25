from django.urls import path

from .views import apply_view

app_name = "jobs"

urlpatterns = [
    path("", apply_view, name="apply"),
]
