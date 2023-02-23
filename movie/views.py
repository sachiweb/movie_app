from django.shortcuts import render,HttpResponse
from ast import Return
from django.http import HttpResponse,HttpResponseRedirect

from .models import Movie


def index(request):
    # moviedata=Movie.objects.all().order_by('title')[:6]
    topdata=Movie.objects.all().filter(status="TR").order_by('title')[:6]
    mostdata=Movie.objects.all().filter(status="MW").order_by('title')[:6]
    adddata=Movie.objects.all().filter(status="RA").order_by('title')[:6]
    data={
        'mostdata':mostdata,
        'topdata':topdata,
        'adddata':adddata
    }
    return render(request,"index.html",data)

def about(request,title):
    moviedata=Movie.objects.get(title=title)
    data={
        'moviedata':moviedata
    }
    return render(request,"about.html",data)

def toprate(request):
    moviedata=Movie.objects.all().filter(status="TR")
    data={
        'moviedata':moviedata
    }
    return render(request,"toprate.html",data)

def most(request):
    moviedata=Movie.objects.all().filter(status="MW")
    data={
        'moviedata':moviedata
    }
    return render(request,"most.html",data)

def latest(request):
    moviedata=Movie.objects.all().filter(status="RA")
    data={
        'moviedata':moviedata
    }
    return render(request,"latest.html",data)

def search(request):
    if request.method=="POST":
        n1=request.POST.get('search field')
        moviedata=Movie.objects.all().filter(title__icontains=n1)
        data={
            'moviedata':moviedata
        }
    else:
        data={"sorry ----- wrong entry"}
    return render(request,"search.html",data)