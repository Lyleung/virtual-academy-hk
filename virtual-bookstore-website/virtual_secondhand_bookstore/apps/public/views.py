# from django.shortcuts import render
#
# # Create your views here.
# migrated from VSB/views.py

# from django.http import HttpResponse
# from django.template import loader
from django.shortcuts import render
from django.http import HttpRequest, HttpResponse


def index(request: HttpRequest) -> HttpResponse:
    # TODO what is Http -> Http
    return render(request, "index.html")


def about(request: HttpRequest) -> HttpResponse:
    return render(request, "about.html")


def contact(request: HttpRequest) -> HttpResponse:
    return render(request, "contact.html")
