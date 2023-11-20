from django.db import models


class Tag(models.Model):
    name = models.CharField(max_length=128, verbose_name='Имя тега')
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")

    class Meta:
        verbose_name = 'Теги'
        verbose_name_plural = 'Теги'

    def __str__(self):
        return self.name


class Person(models.Model):
    name = models.CharField(max_length=128, verbose_name="Имя")
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")
    content = models.TextField(verbose_name="О себе")
    photo = models.ImageField(upload_to="photos/%Y/%m/%d/", verbose_name="Фото")
    contacts_vk = models.URLField(blank=True, verbose_name="VK")
    contacts_tg = models.URLField(blank=True, verbose_name="telegram")

