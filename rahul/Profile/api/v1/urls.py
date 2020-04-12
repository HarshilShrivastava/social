from django.urls import path
from Profile.api.v1.views import(
    CustumerProfile
)
urlpatterns=[
    path('Profile/',CustumerProfile.as_view()),

]