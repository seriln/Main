# Create your views here.
from datetime import datetime
from django.shortcuts import render
import os

def home(request):
    context={'ts':datetime.now(),}
    return render(request, 'home.html', context)

def listing(request,dir):
    dir = '/home/seriln/Projects/'+dir
    os.chdir(dir)
    context = {'dir_content':os.listdir(dir),}
    return render(request, 'listing.html', context)
