from rest_framework import serializers
from .models import Tweet


class TweetSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    payload = serializers.CharField(max_length=180)
    user = serializers.CharField(source="user.username")
    created_at = serializers.DateTimeField()
