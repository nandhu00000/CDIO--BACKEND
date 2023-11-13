from django.shortcuts import render
from django.http import HttpResponse
from.models import summa


# Create your views here.
def show (request):
    return HttpResponse("<h2>Thak You !!!</h2>")
 
def show_num (request,id):
    return HttpResponse(id)
def insert(request):
    s=summa()
    s.descrip = "thi"
    s.name="NANDHU"
    s.save()
    return HttpResponse("<h2>WORTH THU VARMA !!!</h2>")
zero ={}
zero['PARK'] = 'PARK--OR'

def html(request):
    return render (request,"test.html")
