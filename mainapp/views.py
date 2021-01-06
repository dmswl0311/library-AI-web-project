from django.shortcuts import render
from django.db.models import Q
from .models import LibraryList
from django.http import HttpResponse,JsonResponse
from django.views.decorators.csrf import csrf_exempt

def index(request):
    queryset=LibraryList.objects.all()
    query=Q()
    #여성, 10대이하~60대이상까지 인기카테고리 1,2,3위에 있는 첫번째 추천도서 리스트
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
    # gender = request.GET.getlist('gender[]')
    # age = request.GET.getlist('age[]')
    gender=request.GET['gender']
    age=request.GET['age']
    print(age)
    category_name=request.GET.getlist('category_name[]')
    year=request.GET['year']

    query=Q()
    # for i in gender:
    #     query=query|Q(gender__icontains=i)
    #     queryset=queryset.filter(query)
    # for i in age:
    #     query=query|Q(age__icontains=i)
    #     queryset=queryset.filter(query)
    for i in category_name:
        query=query|Q(category_name__icontains=i)
        queryset=queryset.filter(query)
    
    queryset=queryset.filter(Q(gender__icontains=gender)&Q(age__icontains=age))
    # result=queryset.filter(year__range=(2009,int(year))).values('book_name','explain','url').distinct()
    result=queryset.filter(year__range=(2009,int(year))).values('book_name','explain','url').distinct()

    context={
        'library_list':result,
    }
    return render(request,'search_result.html',context)