from django.db import models


class Category(models.Model):
    """Модель категорий"""
    name = models.CharField("Название", max_length=128)
    about = models.TextField("Описание", blank=True)

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"


class Genre(models.Model):
    """Модель жанра"""
    name = models.CharField("Название", max_length=128)
    about = models.TextField("Описание", blank=True)

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = "Жанр"
        verbose_name_plural = "Жанр"


class Participant(models.Model):
    """Модель участников"""
    name = models.CharField("Имя", max_length=128)
    surname = models.CharField("Фамилия", max_length=128)
    age = models.PositiveSmallIntegerField("Возраст", blank=True, null=True)
    about = models.TextField("Описание", blank=True)
    img = models.ImageField("Фотография", upload_to='participants/', blank=True)
    role = models.CharField("Роль", max_length=128)

    def __str__(self):
        return f"{self.name} {self.surname} ({self.role})"

    class Meta:
        verbose_name = "Участники"
        verbose_name_plural = "Участники"


class Movie(models.Model):
    """Модель фильма"""
    name = models.CharField("Название", max_length=128)
    about = models.TextField("Описание", blank=True)
    img = models.ImageField("Постер", upload_to='movies/', blank=True)
    year = models.PositiveSmallIntegerField("Год", blank=True, null=True)
    budget = models.PositiveBigIntegerField("Бюджет", blank=True, null=True)
    country = models.CharField("Срана", max_length=128, blank=True)
    actors = models.ManyToManyField(Participant, verbose_name="Актеры", related_name="film_actors", blank=True)
    directors = models.ManyToManyField(Participant, verbose_name="Продюсер", related_name="film_directors", blank=True)
    genres = models.ManyToManyField(Genre, verbose_name="Жанр", related_name="film_genres", blank=True)
    category = models.ManyToManyField(Category, verbose_name="Категория", related_name="film_category", blank=True)
    video = models.FileField("Видео", upload_to="videos/", blank=True)
    is_active = models.BooleanField("Активный", default=False, db_index=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Фильм"
        verbose_name_plural = "Фильмы"
