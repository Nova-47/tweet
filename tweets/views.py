from django.shortcuts import render
from .models import Tweet  # Tweet 모델 가져오기


def tweet_list(request):
    tweets = Tweet.objects.all()  # ORM을 사용하여 모든 Tweet 가져오기
    return render(
        request,
        "tweet_list.html",
        {
            "tweets": tweets,
            "title": "Twit List",
        },
    )  # 템플릿에 데이터 전달
