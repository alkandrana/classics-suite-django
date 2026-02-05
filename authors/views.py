from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import  Author
# Create your views here.
def main(request):
    template = loader.get_template("main.html")
    return HttpResponse(template.render())
def authors(request):
    authors = Author.objects.all().values()
    template = loader.get_template("list.html")
    context = {
        'authors': authors,
    }
    return HttpResponse(template.render(context, request))

def details(request, id):
    author = Author.objects.get(id=id)
    template = loader.get_template("details.html")
    context = {
        'author': author,
    }
    return HttpResponse(template.render(context, request))