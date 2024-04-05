from django.contrib.auth import authenticate, login
from django.http import HttpRequest
from django.shortcuts import render, redirect
from django.urls import reverse


def login_view(request: HttpRequest):
    if request.method == "GET":
        if request.user.is_authenticated:
            return redirect(reverse('questionnaire:enter'))

    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect(reverse('questionnaire:enter'))
        else:
            error_message = "Invalid username or password. Please try again."
            return render(request, 'auth_user/login.html', {'error_message': error_message})

    return render(request, 'auth_user/login.html')