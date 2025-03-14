from rest_framework import serializers
from .models import Tweet


class TweetSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField()

    class Meta:
        model = Tweet
        fields = ["id", "payload", "user", "created_at"]
