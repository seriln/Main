# Create your views here.
from datetime import datetime
from django.shortcuts import render
from library.models import Image
import os
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response


def home(request):
    context={'images':Image.objects.get(id__exact=1),}
    return render(request, 'home.html', context)

def result(request):
    if request.method == 'POST':
        n = request.POST.get('name','')
        d = request.POST.get('desc','')
        img = request.POST.get('file','')
        newItem = Image(name = n, definition = d, image=img)
        newItem.save()
   
      
        handle_uploaded_file(request.FILES['file'])
    return render(request,'result.html')

def handle_uploaded_file(f):
    destination = open('./galery/media/images/'+f.name, 'wb+')
    for chunk in f.chunks():
        destination.write(chunk)
    destination.close()
