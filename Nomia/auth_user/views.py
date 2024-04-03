from django.contrib.auth import authenticate
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect


def login_view(request: HttpRequest):
    # if request.method == "GET":
    #     if request.user.is_authenticated:
    #         return redirect('login.html')

    return render(request, 'auth_user/login.html')

    # username = request.POST['username']
    # password = request.POST['password']
    #
    # user = authenticate(request, username=username, password=password)
    #
    # if user is not None:
    #     login(request, user)
    #     pass

    return ... # переход на создание нового заведения

