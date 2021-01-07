from django.shortcuts import render
from django.db.models import Q
from .models import LibraryList
from django.http import HttpResponse,JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.core.paginator import Paginator

def index(request):
    queryset=LibraryList.objects.all()
    paginator = Paginator(queryset,30) 
    now_page = request.GET.get('page')
    posts = paginator.get_page(now_page) 

    query=Q()
    # 여성, 10대이하~60대이상까지 인기카테고리 1,2,3위에 있는 첫번째 추천도서 리스트
    for i in range(1,7):
        query=query|Q(age__icontains=(i*10))
        for j in range(1,4):
            query=query|Q(age__icontains=j)
            queryset=queryset.filter(query)
    library_list_f=queryset.filter(Q(gender__icontains='F')&Q(rank__icontains=1))

    queryset=LibraryList.objects.all()
    query=Q()

    #남성, 10대이하~60대이상까지 인기카테고리 1,2,3위에 있는 첫번째 추천도서 리스트
    for i in range(1,7):
        query=query|Q(age__icontains=(i*10))
        for j in range(1,4):
            query=query|Q(age__icontains=j)
            queryset=queryset.filter(query)
    library_list_m=queryset.filter(Q(gender__icontains='M')&Q(rank__icontains=1))

    context={
        'library_list_f':library_list_f,
        'library_list_m':library_list_m,
    }
    return render(request,'index.html',context)

def search_result(request):
    queryset=LibraryList.objects.all()
    queryset2=LibraryList.objects.all()
    age = request.GET.getlist('age[]')
    gender=request.GET['gender']
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

    # result2=queryset.filter(Q(gender__icontains=gender)).distinct()
    context={
        'library_list':result,
    }
    return render(request,'search_result.html',context)

def search(request): 
    search_name = request.GET['search'] 
    lists = LibraryList.objects.filter(book_name__icontains=search_name) 
    context={
        "lists":lists
    } 
    return render(request,"search.html",context)