from django.shortcuts import render
from .models import place, people
from django.http import HttpResponse


# Create your views here.
def fun1(request):
    obj=place.objects.all()
    obj1=people.objects.all()
    return render(request,"index.html",{'result':obj,'result1':obj1})
