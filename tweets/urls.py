from django.urls import path
from .views import AllTweetsView, UserTweetsView

urlpatterns = [
    path("tweets/", AllTweetsView.as_view(), name="all_tweets"),
]
