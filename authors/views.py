from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from django.views.decorators.http import require_POST

from .forms import AuthorForm
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

def add_author(request):
    action = 'add'
    template = loader.get_template("add_author.html")
    if request.method == "POST":
        form = AuthorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('authors')
        else:
            return HttpResponse(template.render({"form": form, 'action': action}, request))
    else:
        form = AuthorForm()
        return HttpResponse(template.render({'form': form, 'action': action}, request))

def edit_author(request, author_id):
    action = 'edit'
    author = Author.objects.get(id=author_id)
    if request.method == "POST":
        form = AuthorForm(request.POST, instance=author)
        if form.is_valid():
            form.save()
            return redirect('authors')
    else:
        form = AuthorForm(instance=author)
    return render(request, 'add_author.html', {'form': form, 'action': action})

@require_POST
def delete_author(request, author_id):
    author = Author.objects.get(id=author_id)
    if author:
        author.delete()
        return redirect('authors')
    else:
        print("Author not found")
        return redirect('authors')