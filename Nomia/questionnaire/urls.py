from django.urls import path

from .views import EnterView, CreateInstitution, Accaunt

app_name = "questionnaire"

urlpatterns = [
    path("enter/", EnterView.as_view(), name="enter"),
    path("create/", CreateInstitution.as_view(), name="create"),
    path("account/", Accaunt.as_view(), name="account")

]
