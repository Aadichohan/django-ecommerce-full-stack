from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, JsonResponse
from django.contrib.auth import authenticate, login
from django.contrib import messages
from daraz.models import User
from helper.global_helper import dictArrayToDict


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

def userList(request):
    user_list = User.objects.values()
    user_list = list(user_list)
    # print(user_list)
    return render(request, 'user/user_list.html', {'user_list': user_list})

def userEdit(request, id= None):
    if request.method == "GET":
        user_detail = get_object_or_404(User, pk=id)
        return render(request, 'user/edit_user.html', {'user': user_detail})
    elif request.method == "POST":
        # print( dictArrayToDict(request.POST) )
        id       =  id if(id is not None) else request.POST.get('id')
        username = request.POST.get('username')
        email    = request.POST.get('email')
        name     = request.POST.get('name')
        password = request.POST.get('password')

        userCommand = User.objects.filter(id=id).update(username = username, 
                                                        email = email, 
                                                        name = name, 
                                                        password = password)
        # print(id)
        if(userCommand > 0):
            messages.add_message(request, messages.SUCCESS, 'Record saved successfully.', extra_tags='success')
            return redirect('user_list')  
        else:
            # messages.error(request, {'danger':'Invalid Username or Password or no changes made.'})
            messages.add_message(request, messages.ERROR, 'Invalid Username or Password or no changes made.', extra_tags='danger')

            # Render the current form again with the error message
            return render(request, 'user/edit_user.html', {'user': dictArrayToDict(request.POST) })
    return redirect('user_list')
        
        