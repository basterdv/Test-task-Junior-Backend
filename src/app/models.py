from django.db import models

class Post(models.Model):
    """
       Модель для хранения медиа-объектов из Instagram.
    """
    insta_id = models.CharField(
        max_length=255,
        unique=True,
        verbose_name='Instagram ID',
        help_text='Уникальный ID поста Instagram',
    )
