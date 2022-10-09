from django.shortcuts import render

#from django.http import HttpResponse
# Create your views here.
def index(request):
    return render(request,'home.html',{'name':'Prabhu Teja'})

def about(request):
    return render(request,'about.html')

def add(request):
    val1=int(request.POST['fname'])
    val2=int(request.POST['lname'])
    res=val1+val2
    return render(request,"result.html",{'result':res})

def aboutDetails(request):
    f_name=request.POST['fname']
    return render(request,"aboutDetails.html",{'name':f_name})