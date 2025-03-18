from django.apps import apps
from rest_framework import serializers
from .models import User


class TinyUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            "name",
            "username",
        )


class PublicOneUserSerializer(TinyUserSerializer):
    tweets = serializers.SerializerMethodField()

    def get_tweets(self, obj):
        # 함수 내에서 임포트하여 순환 참조 방지
        from tweets.serializers import TweetSerializer

        tweets = obj.tweets.all()  # related_name="tweet" 덕분에 접근 가능
        return TweetSerializer(tweets, many=True, context=self.context).data

    class Meta:
        model = User
        fields = TinyUserSerializer.Meta.fields + ("tweets",)


class PrivateUserSerializer(serializers.ModelSerializer):
    gender = serializers.CharField(required=False, default="not_specified")
    language = serializers.CharField(required=False, default="en")
    currency = serializers.CharField(required=False, default="USD")

    class Meta:
        model = User
        exclude = (
            "password",
            "is_superuser",
            "id",
            "is_staff",
            "is_active",
            "first_name",
            "last_name",
            "groups",
            "user_permissions",
        )
