from django.urls import path
from tweets.views import UserTweetsView

urlpatterns = [
    path("users/<int:user_id>/tweets/", UserTweetsView.as_view(), name="user_tweets"),
]
