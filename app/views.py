from django.shortcuts import redirect, render
from .models import *

# Create your views here.
def adminedit(request):
    item=items.objects.filter(id=2)
    return render(request,"adminedit.html",{'item':item})


def modeledit(request):

    item=items.objects.get(id=2)
    item.modelname=request.POST.get('modelname',item.modelname)
    item.description=request.POST.get('description',item.description)
    item.gib=request.FILES.get('gib',item.gib)
    item.price=request.POST.get('price',item.price)
    item.types=request.POST.get('types',item.types)
    item.format=request.POST.get('format',item.format)
    item.modeltype=request.POST.get('modeltype',item.modeltype)
    item.category=request.POST.get('category',item.category)
    item.fbx=request.FILES.get('fbx',item.fbx)
    
    item.save()
    return redirect('adminedit')