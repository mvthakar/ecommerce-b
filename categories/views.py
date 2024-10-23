from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect

from categories.models import Category

# Create your views here.
def list(request: HttpRequest) -> HttpResponse:
    categories = Category.objects.all()
    return render(request, 'list.html', { 'categories': categories })

def add(request: HttpRequest) -> HttpResponse:
    if request.method == 'GET':
        return render(request, 'add.html')

    name = request.POST['name']
    if name.strip() == '':
        return HttpResponse('Name cannot be empty')

    Category.objects.create(name=name)
    return redirect('list')

def edit(request: HttpRequest) -> HttpResponse:
    if request.method == 'GET':
        id = request.GET['id']
        try:
            category = Category.objects.get(id=id)
        except Category.DoesNotExist:
            return HttpResponse("Specified category doesn't exist")
        
        return render(request, 'edit.html', { 'category': category })
    
    id = request.POST['id']
    name = request.POST['name']
    if name.strip() == '':
        return HttpResponse('Name cannot be empty')

    try:
        category = Category.objects.get(id=id)
    except Category.DoesNotExist:
        return HttpResponse("Specified category doesn't exist")
    
    category.name = name
    category.save()
    
    return redirect('list')

def delete(request: HttpRequest) -> HttpResponse:
    id = request.GET['id']
    try:
        category = Category.objects.get(id=id)
    except Category.DoesNotExist:
        return HttpResponse("Specified category doesn't exist")
    
    category.delete()
    return redirect('list')
