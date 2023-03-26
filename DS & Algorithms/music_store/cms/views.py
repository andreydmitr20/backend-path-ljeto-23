from django.shortcuts import render
from .models import Service


def pricing(request):
    """pricing"""
    services = Service.objects.all()
    return render(request, "cms/pricing.html", {"services": services})


def service(request, service_id):
    """service"""
    service = Service.objects.get(pk=service_id)
    return render(request, "cms/service.html", {"service": service})
