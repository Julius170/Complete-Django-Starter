from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return render(request, "hello/index.html")

def phenzic(request):
    return HttpResponse("Sup Phenzic")


def greet(requset, name):
    return render(requset, "hello/greet.html", {
        "name": name.capitalize()
    })