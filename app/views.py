from django.shortcuts import render

def index(request):
    activeStatus=True
    return render(request,'app/aboutOne.html',{'activestatus':activeStatus})

def resume(request):
    activeStatus=True
    return render(request,'app/resumeOne.html',{'activestatus':activeStatus})

def portfolio(request):
    activeStatus=True
    return render(request,'app/portfiloTwo.html',{'activestatus':activeStatus})

def blogs(request):
    activeStatus=True
    return render(request,'app/blogOne.html',{'activestatus':activeStatus})


def contact(request):
    activeStatus=True
    return render(request,'app/contactOne.html',{'activestatus':activeStatus})