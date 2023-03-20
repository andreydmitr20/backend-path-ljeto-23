from urllib import response
from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.views import APIView
from drf_yasg.utils import swagger_auto_schema
from rest_framework.decorators import api_view
from drf_yasg import openapi
from .models import Question, Choice
from django.template import loader
from django.shortcuts import get_object_or_404, render


@api_view(["GET"])
def index(request):
    """hello"""

    latest_question_list = Question.objects.order_by("-pub_date")[:5]
    template = loader.get_template("polls/index.html")
    context = {
        "latest_question_list": latest_question_list,
    }
    return HttpResponse(template.render(context, request))


@api_view(["GET"])
def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, "polls/detail.html", {"question": question})


@api_view(["GET"])
def results(request, question_id):
    response = "You are looking at the result of question  %s"
    return HttpResponse(response % question_id)


@api_view(["GET"])
def vote(request, question_id):
    return HttpResponse("You are voting on question %s" % question_id)
