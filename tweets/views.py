from django.http import JsonResponse
from django.core.exceptions import ObjectDoesNotExist
from .models import Tweet
from users.models import User
from .serializers import TweetSerializer


def all_tweets(request):
    tweets = Tweet.objects.all()
    serializer = TweetSerializer(tweets, many=True)
    return JsonResponse(serializer.data, safe=False)  # JSON 응답


def user_tweets(request, user_id):
    try:
        user = User.objects.get(id=user_id)  # 유저 찾기
        tweets = Tweet.objects.filter(user=user)
        serializer = TweetSerializer(tweets, many=True)
        return JsonResponse(serializer.data, safe=False)
    except User.DoesNotExist:  # 유저가 존재하지 않으면 404 반환
        return JsonResponse({"error": "User not found"}, status=404)
