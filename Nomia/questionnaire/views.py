from django.http import HttpRequest
from django.shortcuts import render


def test_view(request: HttpRequest):
    return render(request, 'questionnaire/base.html')
