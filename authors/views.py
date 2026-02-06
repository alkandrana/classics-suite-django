from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from django.views.decorators.http import require_POST, require_GET

from .forms import AuthorForm, WorkForm
from .models import  Author, Opus
# Create your views here.

### AUTHORS ###
def main(request):
    template = loader.get_template("main.html")
    return HttpResponse(template.render())
def authors(request):
    authors = Author.objects.all()
    template = loader.get_template("authors/list.html")
    context = {
        'authors': authors,
    }
    return HttpResponse(template.render(context, request))

def details(request, id):
    author = Author.objects.get(id=id)
    template = loader.get_template("authors/details.html")
    context = {
        'author': author,
    }
    return HttpResponse(template.render(context, request))

def add_author(request):
    action = 'add'
    template = loader.get_template("authors/add.html")
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
    return render(request, 'authors/add.html', {'form': form, 'action': action})

@require_POST
def delete_author(request, author_id):
    author = Author.objects.get(id=author_id)
    if author:
        author.delete()
        return redirect('authors')
    else:
        print("Author not found")
        return redirect('authors')

### OPERA ###
@require_GET
def opera(request):
    opera = Opus.objects.all()
    authors = Author.objects.all()
    if request.GET and request.GET["search"]:
        opera = Opus.objects.filter(author__id=int(request.GET["search"]))
    return render(request, 'works/list.html', {'opera': opera, 'authors': authors})

def add_work(request, author_id=None):
    action = 'add'
    if request.method == "POST":
        form = WorkForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('opera')
    else:
        if author_id:
            author = Author.objects.get(id=author_id)
            if author:
                form = WorkForm(initial={'author': author_id, 'dialect': author.language})
        else:
            form = WorkForm()
    return render(request, "works/add.html", {'form': form, 'action': action})

def edit_work(request, work_id):
    action = 'edit'
    work = Opus.objects.get(id=work_id)
    if request.method == "POST":
        form = WorkForm(request.POST, instance=work)
        if form.is_valid():
            form.save()
            return redirect('opera')
    else:
        form = WorkForm(instance=work)
    return render(request, "works/add.html", {'form': form, 'action': action})

@require_POST
def delete_work(request, work_id):
    work = Opus.objects.get(id=work_id)
    if work:
        work.delete()
        return redirect('opera')
    else:
        print("Work not found")
        return redirect('opera')
