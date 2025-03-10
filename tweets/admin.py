from django.contrib import admin
from .models import Tweet
from .models import Like


@admin.register(Tweet)
class TweetAdmin(admin.ModelAdmin):

    list_display = (
        "short_payload",
        "user",
        "created_at",
        "updated_at",
        "like_count",
    )
    list_filter = ("user", "created_at")
    search_fields = ("user",)

    def short_payload(self, obj):
        return f"{obj.payload[:4]}..."

    short_payload.short_description = "Payload"


@admin.register(Like)
class LikeAdmin(admin.ModelAdmin):

    list_display = (
        "user",
        "tweet",
        "created_at",
        "updated_at",
    )
    list_filter = ("user", "tweet")
    search_fields = ("user",)
