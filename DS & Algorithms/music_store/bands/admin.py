from django.contrib import admin
from .models import Band, Member


class AdminBand(admin.ModelAdmin):
    """admin model"""

    search_fields = ["name"]
    list_display = ["name", "can_rock", "image"]
    list_filter = ["can_rock"]


class AdminMember(admin.ModelAdmin):
    """admin model"""

    search_fields = ["name"]
    list_display = ["name", "instruments"]
    list_filter = ["instruments"]


admin.site.register(Band, AdminBand)
admin.site.register(Member, AdminMember)
