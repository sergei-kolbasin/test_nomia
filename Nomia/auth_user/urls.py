from django.urls import path

from .views import login_view

app_name = "auth_user"

urlpatterns = [
    path(
        "", login_view, name="auth_user")
]
