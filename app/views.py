from django.shortcuts import redirect, render
from .models import *

# Create your views here.
def adminedit(request):
    return render(request,"adminedit.html")


def modeledit(request):
    modelname=request.POST['modelname']
    description=request.POST['description']
    gib=request.FILES['gib']
    price=request.POST['price']
    types=request.POST['types']
    format=request.POST['format']
    modeltype=request.POST['modeltype']
    category=request.POST['category']
    fbx=request.FILES['fbx']
    var=items(modelname=modelname,description=description,gib=gib,price=price,types=types,format=format,modeltype=modeltype,category=category,fbx=fbx)
    var.save()
    return redirect('adminedit')