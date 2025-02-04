from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, JsonResponse
from django.contrib.auth import authenticate, login
from daraz.models import User

# Create your views here.

def userLogin(request):
    if request.method == "GET":
        return render(request, 'User/login.html')
    elif request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            print('data ',user)
            return redirect('dashboard')
        else:
            return HttpResponse('Invalid Username or Password')
    return render(request, 'login.html')
        
        
        

def dashboard(request):
    return render(request, 'dashboard/home.html')

def userList(request):
    user_list = User.objects.values()
    user_list = list(user_list)
    print(user_list)
    return render(request, 'user/user_list.html', {'user_list': user_list})

def userEdit(request, id= None):
    if request.method == "GET":
        user_detail = get_object_or_404(User, pk=id)
        return render(request, 'user/edit_user.html', {'user': user_detail})
    elif request.method == "POST":
        print(request.body)
        return HttpResponse('Post')
