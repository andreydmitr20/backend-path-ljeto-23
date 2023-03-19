from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.views import APIView
from drf_yasg.utils import swagger_auto_schema
from rest_framework.decorators import api_view
from drf_yasg import openapi


@api_view(["GET"])
def index(request):
    print(request)
    return HttpResponse("Hello, world. You're at the polls index.")
