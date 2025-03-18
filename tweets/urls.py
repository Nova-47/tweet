from django.urls import path
from .views import AllTweetsView, DetailTweetsView

urlpatterns = [
    path("tweets/", AllTweetsView.as_view(), name="all_tweets"),
    path("tweets/<int:pk>/", DetailTweetsView.as_view(), name="all_tweets"),
]
