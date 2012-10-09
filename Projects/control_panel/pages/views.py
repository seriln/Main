# Create your views here.
from datetime import datetime
from django.shortcuts import render
from library.models import Author, Book
import os

def home(request):
    context={'ts':datetime.now(),}
    return render(request, 'home.html', context)

def listing(request,dir):
    dir = '/home/seriln/Projects/'+dir
   
    dirs = []
    files = []

    for dirNames, dirName, file in os.walk(dir):
        if (dirNames==dir):
            os.chdir(dir)
            for i in file:
                files.append({'name':i, 'size': os.path.getsize(i), 'modtime':datetime.fromtimestamp(int(os.path.getmtime(i))),})
            dirs = dirName

    context = {'dir_content':dirs,'file_content':files,}
    return render(request, 'listing.html', context)

def book(request,ffff):
    context = {'book':Book.objects.all(),}
    return render(request, 'book.html', context)

def bookinfo(request,N):
    bk = Book.objects.get(id__exact=N[:-1])
    context = {'bookinfo':bk, 'book_author': bk.authors.all(),}
    return render(request, 'bookinfo.html', context)

def author(request,N):
    context = {'author':Author.objects.get(id__exact=N[:-1]),}
    return render(request, 'author.html', context)
