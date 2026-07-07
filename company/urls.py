from django.urls import path

from .views import CompanyListView

app_name = "company"

urlpatterns = [
    path("company_list/", CompanyListView.as_view(), name="company_list"),
]
