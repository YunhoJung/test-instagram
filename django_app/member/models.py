from django.contrib.auth.models import AbstractUser
from django.db import models


# User = get_user_model() -> AUTH_USER_MODEL를 받는다 없으면 기본 유저를 받는다.

class User(AbstractUser):
    pass

# User를 customizing하기 위해 이렇게 한다.
