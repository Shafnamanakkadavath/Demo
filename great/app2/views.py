from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def fun1(request):
    return HttpResponse("HOME")
def fun2(request):
    return render(request,"about.html")
def fun3(request):
    return HttpResponse("Contact")
def fun4(request):
    return render(request,"Details.html")
def fun5(request):
    return HttpResponse("THANKS")