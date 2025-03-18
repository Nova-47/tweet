from django.urls import path
from tweets.views import UserTweetsView
from .views import PublicOneUser, PublicAllUser

urlpatterns = [
    path("users/", PublicAllUser.as_view()),
    path("users/<int:pk>/", PublicOneUser.as_view()),
    path("users/<int:pk>/tweets/", UserTweetsView.as_view()),
]
