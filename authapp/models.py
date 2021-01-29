from django.db import models
from django.contrib.auth.models import AbstractUser


class FilmUser(AbstractUser):
    MALE = 'M'
    FEMALE = 'W'

    GENDER_CHOICES = (
        (MALE, 'мужской'),
        (FEMALE, 'женский'),
    )

    age = models.IntegerField(verbose_name="Возраст", null=True, blank=True)
    gender = models.CharField(verbose_name='пол', max_length=1, choices=GENDER_CHOICES, blank=True)
