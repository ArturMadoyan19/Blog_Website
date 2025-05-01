from django.shortcuts import render, redirect
from .models import User
import json
from django.http import JsonResponse


def ui(request):
    return render(request, 'registration/reg.html')

def user_info(request):
    if request.method == "POST":
        data = request.POST
        name = data['name']
        surname = data['surname']
        username = data['username']
        email = data['email']
        password = data['password']
        response = {}
        check = {}
        check_true = True
        users = list(User.objects.values())
        for user in users:
            if user['username'] == str(username):
                check["status"] = "Write another username"
                check_true = False
            if len(password) < 6:
                check["status"] = "Password len >6"
                check_true = False
        if name and surname and username and email and password and check_true:
            user = User.objects.create(
                name = name,   
                surname = surname,
                username = username,
                email = email,
                password = password
                )
            return redirect('login')
        
    response["status"] = "Only POST allowed"
    return render(request, 'registration/reg.html',{'response':response, 'check':check, 'name':name,'surname':surname,'username':username,'email':email})


def get_user(request):
    users = list(User.objects.values())
    return JsonResponse(users, safe=False)

def clean_db(request):
    delete = User.objects.all().delete()
    return JsonResponse(delete,safe=False)
