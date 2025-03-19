from django.urls import path
from tweets.views import UserTweetsView
from .views import PublicOneUser, PublicAllUser, ChangePassword, LogIn, LogOut

urlpatterns = [
    path("users/", PublicAllUser.as_view()),
    path("change-password", ChangePassword.as_view()),
    path("users/log-in/", LogIn.as_view()),
    path("users/log-out/", LogOut.as_view()),
    path("users/<int:pk>/", PublicOneUser.as_view()),
    path("users/<int:pk>/tweets/", UserTweetsView.as_view()),
]
