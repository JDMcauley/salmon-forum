from django.shortcuts import render
from django.http import HttpResponse

# def index(response):
#     return render(response, "forum/base.html")
def index(request):
    return HttpResponse("Hello world!")

def home(response):
    return render(response, "forum/home.html", {})