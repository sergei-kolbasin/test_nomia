from django.urls import path

from .views import test_view

app_name = "questionnaire"

urlpatterns = [
    path(
        "hi/", test_view, name="test")
]
