from django.urls import path, include
from django.urls import path
from . import views

urlpatterns = [
    path("tweets/", views.all_tweets, name="all_tweets"),  # 모든 트윗 리스트
]
