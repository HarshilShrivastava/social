from django.urls import path
from Profile.api.v1.views import(
    CustumerProfile,
    StatusView,
    StatusViewDetail
)
urlpatterns=[
    path('Profile/',CustumerProfile.as_view()),
    path('Status/',StatusView.as_view()),
    path('StatusDetail/<int:pk>',StatusViewDetail.as_view()),

]