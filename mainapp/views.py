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
    gender = request.GET['gender']
    age = request.GET['age']
    year=request.GET['year']
    result = queryset.filter(Q(gender__icontains=gender)&Q(age__icontains=age)&Q(year__icontains=year))
    context={
        'library_list':result,
    }
    return render(request,'search_result.html',context)