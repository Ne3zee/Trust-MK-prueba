from django.contrib import admin

from .models import Application


@admin.register(Application)
class ApplicationAdmin(admin.ModelAdmin):
    list_display = ("full_name", "phone", "email", "age", "availability", "created_at")
    list_filter = ("availability", "created_at")
    search_fields = ("full_name", "phone", "email")
