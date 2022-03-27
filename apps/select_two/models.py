from django.db import models
from django.contrib.postgres.fields import ArrayField


class Language(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.title


class Entry(models.Model):
    language = models.ForeignKey(Language, on_delete=models.CASCADE, verbose_name="Favourite Language")
    name = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.name


class EntryName(models.Model):
    language = models.ManyToManyField(Language, verbose_name="Favourite Language")
    name = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.name


class Country(models.Model):
    # ArrayField only for postgres database
    name = ArrayField(ArrayField(models.CharField(max_length=10, blank=True), size=8,), size=8,)
