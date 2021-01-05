from django.shortcuts import render
from django.db.models import Q
from .models import LibraryList

def index(request):
    library_list = LibraryList.objects.all()
    context={
        'library_list':library_list,
    }
    return render(request,'index.html',context)

def search_result(request):
    queryset=LibraryList.objects.all()
    gender = request.GET.getlist('gender[]')
    age = request.GET.getlist('age[]')
    # year=request.GET.getlist('year[]')
    year=request.GET['year']
    query=Q()
    for i in gender:
        query=query|Q(gender__icontains=i)
        queryset=queryset.filter(query)
    for i in age:
        query=query|Q(age__icontains=i)
        queryset=queryset.filter(query)
        
    result=queryset.filter(year__range=(2009,int(year)))

    context={
        'library_list':result,
    }
    return render(request,'search_result.html',context)