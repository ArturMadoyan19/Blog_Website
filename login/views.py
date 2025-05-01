from django.shortcuts import render, redirect
from registration.models import User
import json
from django.http import JsonResponse

def login_ui(request):
    return render(request,'login/login_view.html')

def check_login(request):
    if request.method == 'POST':
        data = request.POST
        login = data['login']
        password = data['password']
        response = {}
        try:
            user = User.objects.filter(username=login).first()
            if user:
                if user.password == password:
                    # remember = data['remember_me']
                    # if not remember:
                    #     request.session.set_expiry(0)
                    # else:
                    #     request.session.set_expiry(60*60*24*30)
                    response["status"] = "succsess"
                    response["user_id"] = user.id
                    request.session['username'] = user.username
                    return redirect('post_ui')
                else:
                    response["status"] = "Incorrect password"
                    return render(request,'login/login_view.html', {'response':response,'login_value':login})
            else:
                response["status"] = "Incorrect Username"
                return render(request,'login/login_view.html', {'response':response,'login_value':login})       
        except User.DoesNotExist:
            return JsonResponse({'status': 'error', 'message': 'User not found'})