from django.http import HttpResponse
from django.shortcuts import render, HttpResponse
from home.models import Conection_eg
from django.template import loader

# Create your views here.

def index(request):
    
    context ={
        'variable1':"This is sent"
    }
    return render(request, 'index.html',context)

def about(request):

    mymembers = Conection_eg.objects.all().values()
    template = loader.get_template('about.html')
    context = {
        'mymembers': mymembers,
    }
    return HttpResponse(template.render(context, request))

    

def services(request):
    return render(request, 'services.html')

def contact(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        desc = request.POST.get('desc')
        conection_eg = Conection_eg(firstname=email, lastname=desc)
        conection_eg.save()
        return render(request, 'contact.html')