from django.urls import path
from . import views

app_name = "cms"
urlpatterns = [
    path("pricing/", views.pricing, name="pricing"),
    path("service/<int:service_id>", views.service, name="service"),
]
