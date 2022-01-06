from django.shortcuts import render
from django.http import HttpResponse
from .models import product
# Create your views here.

def index(request):
    products=product.objects.all()
    return render(request,'index.html',{'products':products})

   # return HttpResponse("<h1> welcome to django </h1>")
def about(request):
    return HttpResponse("<h1>about paragraph</h1>")