from django.contrib import admin
from .models import Service


class AdminService(admin.ModelAdmin):
    """admin model"""

    search_fields = ["name"]
    list_display = ["name", "description", "image", "price"]


admin.site.register(Service, AdminService)
