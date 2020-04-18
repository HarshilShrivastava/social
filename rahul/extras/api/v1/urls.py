from django.urls import path
from extras.api.v1.views import(
    confirm_Profile
)
urlpatterns=[
    path('confirm/',confirm_Profile,name="confirmation"),
]