from django.shortcuts import render, redirect
from .forms import FoodForm
from .models import Food
# from django.contrib.auth.forms import UserCreationForm
# from django.contrib.auth import authenticate,login

from django.contrib import messages

def add_food(request):
    if request.method == 'POST':
        form = FoodForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('food_list')
    else:
        form = FoodForm()
    return render(request, 'trekar/add_food.html', {'form' : form})

def food_list(request):
    foods = Food.objects.all()
    return render(request, 'trekar/food_list.html', {'foods': foods})

def edit_food(request,food_id):
    food = Food.objects.get(id = food_id)
    if request.method == 'POST':
        form = FoodForm(request.POST,instance=food)
        if form.is_valid():
            form.save()
            return redirect('food_list')
    else:
        form = FoodForm()
    return render(request, 'trekar/edit_food.html', {'form' : form})

def delete_food(request, food_id):
    food = Food.objects.get(id = food_id)
    food.delete()
    return redirect('food_list')

# def register(request):
#     if request.method == 'POST':
#         form = UserCreationForm(request.POST)
#         print("hello")
#         if form.is_valid():
#             form.save()
#             Username=form.cleaned_data.get('username')
#             messages.success(request, f'account created for a {Username}')
#             return redirect('Login')
#     else:
#         form=UserCreationForm()
#         return render(request,'registrastion/register.html',{'form':form})
    
# def user_login(request):
#     if request.method == 'POST':
#         form=LoginForm(request.POST)
#         if form.is_valid():
#             form.save()
#         username=form.cleaned_data['username']
#         password=form.cleaned_data['password']
#         user=authenticate(username=username,password=password)
#         if user is not None :
#             login(request,user)
#             return redirect('food_list')
#         else:
#             form.add_error(None,{'error':'not correct password'})
#     else:
#         form=LoginForm
#         return render(request,'registrastion/user_login.html',{'form':'form'})


            


