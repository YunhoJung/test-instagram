from django.db import models

from django.conf import settings

# User = get_user_model() 마찬가지로 동적으로 연동가능.
# 자주 쓰는 모델은 모듈화하는 것이 좋음.
from module.timemixin import TimeMixinStamp


class Post(TimeMixinStamp):
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL)  # 한 사람 당 여러개 post에 접근할 수 있어서 foreinkey(일대다). 다에다가 키를 걸어줘야 함. 이렇게 하면 User모델 동적으로 연동된다
    photo = models.ImageField(upload_to='post-%y%m%d', blank=True)  # 이렇게 하는 이유는 용량 문제 때문.
    like_users = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        through='PostLike',
        related_name='like_users'
    )


# 역참조시 User를 두개로 받고 있어서 related_name으로 바꿔줘야 한다.

class Comment(TimeMixinStamp):
    author = models.ForeignKey(settings.AUTH_USER_MODEL)  # 일상생활에서 foreignkey 관계에 대해 고민해보자.
    post = models.ForeignKey(Post) # 포스트 당 여러 개의 comment를 달 수 있다.
    content = models.TextField()


class PostLike(models.Model):  # m2m필드로 생성될 때 post user가 id값으로 db에 생성되기 때문. 중간값모델을 사용하는 이유는 커스텀마이징(created_date)하고 싶어서
    post = models.ForeignKey(Post)
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    created_date = models.DateTimeField(auto_now_add=True)
