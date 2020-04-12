from django.urls import path,include
from Request.api.v1.views import(
    add_friend_request,
    accept_request,
    reject_request,
    remove_friend,
    list_of_sent_request,
    list_of_recived_request,
    list_of_friends,
)
urlpatterns=[
    path('addrequest/<int:To>/<int:From>',add_friend_request,name="request"),
    path('accept-request/<int:id>',accept_request,name="accept request"),
    path('reject-request/<int:id>',reject_request,name="reject request"),
    path('remove-friend/<int:id>',remove_friend,name="remove friend"),
    path('list-r-request/',list_of_recived_request,name="received request"),
    path('list-s-request/',list_of_sent_request,name="sent request"),
    path('list-all-friends',list_of_friends,name="list of friends"),
]