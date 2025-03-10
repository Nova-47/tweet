from django.db import models


# Create your models here.
class Tweet(models.Model):
    payload = models.TextField(max_length=180)  # 트윗 내용
    user = models.ForeignKey(
        "users.User", on_delete=models.CASCADE, related_name="tweets"
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user.username}: {self.payload[:10]}..."  # 유저명 + 트윗 내용 앞 10자만 표시

    def like_count(self):
        return self.likes.count()  # Like 개수를 반환


class Like(models.Model):
    user = models.ForeignKey("users.User", on_delete=models.CASCADE)
    tweet = models.ForeignKey(Tweet, on_delete=models.CASCADE, related_name="likes")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user.username} liked '{self.tweet.payload[:5]}...'"
