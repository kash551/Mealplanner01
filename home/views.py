# import all libraries
from django.shortcuts import render, redirect, get_object_or_404
from .models import Recipe
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import logout
from django.contrib import messages


# create recipes page
@login_required(login_url='/login/')
def recipes(request):
    if request.method == 'POST':
        data = request.POST
        day = data.get('day')
        name = data.get('name')
        description = data.get('description')
        Recipe.objects.create(
            day=day,
            name=name,
            description=description,
        )
        messages.info(request, "Creation Successful")
        return redirect('/')

    queryset = Recipe.objects.all()
    if request.GET.get('search'):
        queryset = queryset.filter(
            day__icontains=request.GET.get('search')
        )

    context = {'recipes': queryset}
    return render(request, 'recipe.html', context)


# Update the recipes data
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


# delete the recipes data
@login_required(login_url='/login/')
def delete_recipe(request, id):
    recipe = get_object_or_404(Recipe, id=id)

    if request.method == "POST":
        recipe.delete()
        messages.info(request, "Deleted Successfully")
        return redirect('/')

    return render(request, 'confirm_delete.html', {'recipe': recipe})


# login page for user
def login_page(request):
    if request.method == "POST":
        try:
            username = request.POST.get('username')
            password = request.POST.get('password')
            user_obj = User.objects.filter(username=username)
            if not user_obj.exists():
                messages.error(request, "Username not found")
                return redirect('/login/')
            user_obj = authenticate(username=username, password=password)
            if user_obj:
                login(request, user_obj)
                messages.info(request, "Login Successful")
                return redirect('recipes')
            messages.error(request, "Wrong Password")
            return redirect('/login/')
        except Exception as e:
            messages.error(request, "Something went wrong")
            return redirect('/register/')
    return render(request, "login.html")


# register page for user
def register_page(request):
    if request.method == "POST":
        try:
            username = request.POST.get('username')
            password = request.POST.get('password')
            user_obj = User.objects.filter(username=username)
            if user_obj.exists():
                messages.error(request, "Username is taken")
                return redirect('/register/')
            user_obj = User.objects.create(username=username)
            user_obj.set_password(password)
            user_obj.save()
            messages.success(request, "Account created")
            return redirect('/login')
        except Exception as e:
            messages.error(request, "Something went wrong")
            return redirect('/register')
    return render(request, "register.html")


# logout function
def custom_logout(request):
    logout(request)
    messages.info(request, "Logout Successful")
    return redirect('login')


# Generate the PDF
@login_required(login_url='/login/')
def pdf(request):
    if request.method == 'POST':
        data = request.POST
        day = data.get('day')
        name = data.get('name')
        description = data.get('description')

        Recipe.objects.create(
            day=day,
            name=name,
            description=description,
        )
        return redirect('pdf')
    queryset = Recipe.objects.all()

    if request.GET.get('search'):
        queryset = queryset.filter(
            day__icontains=request.GET.get('search')
        )

    context = {'recipes': queryset}
    return render(request, 'pdf.html', context)
