from django.urls import path, include
from django.urls import path
from tweets.views import all_tweets, user_tweets

urlpatterns = [
    path(
        "users/<int:user_id>/tweets/", user_tweets, name="user_tweets"
    ),  # 특정 유저의 트윗 리스트
]
