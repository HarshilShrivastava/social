from django.urls import path
from User.api.v1.views import(
    registration_view,
    login_view,
    
)
urlpatterns = [
    path('register/', registration_view, name='register'),
    path('login/', login_view, name='login'),
]