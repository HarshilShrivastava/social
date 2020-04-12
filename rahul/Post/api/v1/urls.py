from django.urls import path
from Post.api.v1.views import(
    PostView,
    PostViewDetail,
    like,
    CommentView,
    CommentViewDetail
)
urlpatterns=[
    path('Post/',PostView.as_view()),
    path('PostDetail/<int:pk>',PostViewDetail.as_view()),
    path('like/<int:pk>',like),
    path('comment/<int:pk>/',CommentView.as_view()),
    path('commentviewdetail/<int:pk>/<int:id>',CommentViewDetail.as_view()),
]