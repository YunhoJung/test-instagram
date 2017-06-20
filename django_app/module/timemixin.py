from django.db import models

__all__ = [
    'TimeMixinStamp',
]


# import할 것만 모아놓을 수 있음.

class TimeMixinStamp(models.Model):
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True # db 안만들고 상속만 받을거라서
