from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()


class profile(models.Model):
    user = models.ForeignKey(User, verbose_name='Псевдоним', on_delete=models.CASCADE)
    username = models.CharField(max_length=40, verbose_name='Имя пользователя', on_delete=models.CASCADE)
    userfamily = models.
