from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):  # Django 기본 User 모델 확장
    first_name = models.CharField(max_length=150, editable=False)
    last_name = models.CharField(max_length=150, editable=False)
    name = models.CharField(max_length=150, default="")

    def __str__(self):
        return f"@{self.username}"  # "트위터 스타일로 표시"
