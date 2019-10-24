from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings

# Create your models here.
class User(AbstractUser):
    # 연결을 시켜줌
    followers = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="followings") #settings맨밑에서 만들어준 accounts.User 가 들어온다. 