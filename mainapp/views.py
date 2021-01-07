from django.shortcuts import render
from django.db.models import Q
from .models import LibraryList
from django.http import HttpResponse,JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.core.paginator import Paginator

def index(request):
    queryset=LibraryList.objects.all()
    query=Q()
    
    result=queryset.filter(Q(rank='1')).order_by('age','gender').distinct()
    context={
        'library_list_f':result,
    }
    return render(request,'index.html',context)

def search_result(request):
    queryset=LibraryList.objects.all()
    queryset2=LibraryList.objects.all()
    age=[10,20,30,40,50,60]
    gender='F'
    category_name=['과학']

    age = request.GET.getlist('age[]')
    gender = request.GET['gender']
    category_name=request.GET.getlist('category_name[]')
    year1=request.GET['year1']
    year2=request.GET['year2']
    query=Q()
    query2=Q()

    for i in age:
        query=query|Q(age__icontains=i)
        queryset=queryset.filter(query)

    for i in category_name:
        query2=query2|Q(category_name__icontains=i)
        queryset2=queryset2.filter(query2)
    
    result=LibraryList.objects.all().filter(query&query2&Q(gender__icontains=gender))
    result=result.filter(year__range=(int(year1),int(year2))).order_by('rank').distinct()
    cnt=0

    for _ in result:
        cnt+=1

    if gender=='F':
        gender='여성'
    elif gender=='M':
        gender='남성'
    # result2=queryset.filter(Q(gender__icontains=gender)).distinct()
    context={
        'library_list':result,
        'gender':gender,
        'age_list':age,
        'category_list':category_name,
        'year1':year1,
        'year2':year2,
        'count':cnt,
    }
    return render(request,'search_result.html',context)

def search(request): 
    search_name = request.GET['search'] 
    lists = LibraryList.objects.filter(book_name__icontains=search_name).values('book_name','url','explain').distinct()
    cnt=0
    for _ in lists:
        cnt+=1

    context={
        "lists":lists,
        'search_name':search_name,
        'count':cnt,
    } 
    return render(request,"search.html",context)

def test(request):
    queryset=LibraryList.objects.all()
    query=Q()
    
    result=queryset.filter(Q(rank='1')).order_by('age','gender').distinct()
    context={
        'library_list_f':result,
    }
    return render(request,'test.html',context)