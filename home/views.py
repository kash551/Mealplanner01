from django.shortcuts import render, redirect
from .models import Recipe
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required 
from django.contrib.auth.models import User
from django.contrib.auth import logout

# Create recipe page
@login_required(login_url='/login/')
def recipes(request):
    if request.method == 'POST': 
        data = request.POST
        day = data.get('day')
        name = data.get('name')
        description = data.get('description')      
        Recipe.objects.create(
            day = day,
            name=name,
            description=description,        
        )
        return redirect('/')
 
    queryset = Recipe.objects.all()
    if request.GET.get('search'):
        queryset = queryset.filter(
            day__icontains=request.GET.get('search'))
          
    context = {'recipes': queryset}
    return render(request, 'recipe.html', context)

#Update the recipes data 
@login_required(login_url='/login/')
def update_recipe(request, id):
    queryset = Recipe.objects.get(id=id)
 
    if request.method == 'POST':
        data = request.POST   
        day = data.get('day')
        name = data.get('name')
        description = data.get('description')
         
        queryset.day = day
        queryset.name = name
        queryset.description = description
        queryset.save()
        return redirect('/')
 
    context = {'recipe': queryset}
    return render(request, 'update_recipe.html', context)

 #delete the recipes data
@login_required(login_url='/login/')
def delete_recipe(request, id):
    queryset = Recipe.objects.get(id=id)
    queryset.delete()
    return redirect('/')   