from django.urls import path

from .views import (EnterView,
                    CreateInstitution,
                    Account,
                    BusinessType,
                    ServicesType,
                    Catering,
                    RetailType,
                    CateringType,
                    Retail)

app_name = "questionnaire"

urlpatterns = [
    path("enter/", EnterView.as_view(), name="enter"),
    path("create/", CreateInstitution.as_view(), name="create_institution"),
    path("account/", Account.as_view(), name="account"),
    path("type/", BusinessType.as_view(), name="business_type"),
    path("services/", ServicesType.as_view(), name="services_type"),
    path("catering/", Catering.as_view(), name="catering"),
    path("retail/", Retail.as_view(), name="retail"),
    path("retail_type/", RetailType.as_view(), name="retail_type"),
    path("catering_type/", CateringType.as_view(), name="catering_type"),

]
