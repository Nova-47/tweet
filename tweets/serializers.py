from rest_framework import serializers
from .models import Tweet, Like
from users.serializers import TinyUserSerializer


class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = ["id", "user", "tweet", "created_at"]


class TweetSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField()

    class Meta:
        model = Tweet
        fields = ["id", "payload", "user", "created_at"]

    def get_user(self, obj):
        return {"id": obj.user.id, "username": obj.user.username}


class TweetDetailSerializer(serializers.ModelSerializer):

    user = TinyUserSerializer(read_only=True)
    payload = serializers.CharField(required=True)
    like_count = serializers.IntegerField(source="likes.count", read_only=True)
    is_mine = serializers.SerializerMethodField()

    class Meta:
        model = Tweet
        fields = "__all__"

    def get_is_mine(self, obj):
        request = self.context.get("request")
        if request:
            return obj.user == request.user
        return False
