from django.contrib import admin
from .models import Tweet
from .models import Like


class ElonMuskFilter(admin.SimpleListFilter):
    title = "Elon_Filter"
    parameter_name = "elon_musk"

    def lookups(self, request, model_admin):
        return [
            ("contains", "Contains 'Elon Musk'"),
            ("not_contains", "Doesn't contain 'Elon Musk'"),
        ]

    def queryset(self, request, queryset):
        if self.value() == "contains":
            return queryset.filter(payload__icontains="Elon Musk")
        if self.value() == "not_contains":
            return queryset.exclude(payload__icontains="Elon Musk")
        return queryset


@admin.register(Tweet)
class TweetAdmin(admin.ModelAdmin):

    list_display = (
        "short_payload",
        "user",
        "created_at",
        "updated_at",
        "like_count",
    )
    list_filter = ("user__username", "created_at", ElonMuskFilter)
    search_fields = ("user__username",)

    def short_payload(self, obj):
        return f"{obj.payload[:4]}..."


@admin.register(Like)
class LikeAdmin(admin.ModelAdmin):

    list_display = (
        "user",
        "tweet",
        "created_at",
        "updated_at",
    )
    list_filter = ("user__username", "created_at", ElonMuskFilter)
    search_fields = ("user__username", "tweet__payload")
