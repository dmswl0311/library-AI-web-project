from django.shortcuts import render
from django.db.models import Q
from .models import LibraryList

def index(request):
    return render(request,'index.html')

def search_result(request):
    queryset=LibraryList.objects.all()
    gender = request.GET['gender']
    age = request.GET['age']
    result = queryset.filter(Q(gender__icontains=gender)&Q(age__icontains=age))
    context={
        'library_list':result,
    }
    return render(request,'search_result.html',context)