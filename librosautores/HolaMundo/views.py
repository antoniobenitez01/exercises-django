from django.shortcuts import render, redirect
from HolaMundo.models import Author, Book
from HolaMundo.forms import AutorForm

def home(request):
    return render(request,"index.html")

def autor_list (request):
    autor = Author.objects.all()
    return render(request,"autor.html",{ 'authors' : autor })

def libro_list (request):
    libro = Book.objects.all()
    return render(request,"libro.html",{ 'books' : libro })

def autor_create(request):
    if request.method == "GET":
        return render(request, "createautor.html", { 'autor_form' : AutorForm })
    if request.method == "POST":
        form = AutorForm(data=request.POST)
        if form.is_valid:
            form.save()  
        else:
            form = AutorForm(data=request.POST)
            return render(request, "createautor.html", { 'autor_form' : AutorForm })
        
def autor_update(request, pk=None):
    autor = Author.objects.get(pk=pk)
    if request.method == "GET":
        author_form = AutorForm(instance = autor)
        return render (request, "updateautor.html", { 'author' : autor, 'author_form' : author_form})
    if request.method == "POST":
        author_form = AutorForm(data=request.POST, instance=autor)
        if author_form.is_valid():
            author_form.save()
            return redirect('/autor/')
        else:
            author_form = AutorForm(data=request.POST, instance=autor)
            return render (request, "updateautor.html", { 'author' : autor, 'author_form' : author_form})
        
def autor_delete (request, pk=None):
    Author.objects.filter(pk=pk).delete()
    return redirect("/autor")
