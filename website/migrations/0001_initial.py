# Generated by Django 4.2.7 on 2023-11-20 19:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, verbose_name='Имя')),
                ('slug', models.SlugField(max_length=255, unique=True, verbose_name='URL')),
                ('content', models.TextField(verbose_name='О себе')),
                ('photo', models.ImageField(upload_to='photos/%Y/%m/%d/', verbose_name='Фото')),
                ('contacts_vk', models.URLField(blank=True, verbose_name='VK')),
                ('contacts_tg', models.URLField(blank=True, verbose_name='telegram')),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, verbose_name='Имя тега')),
                ('slug', models.SlugField(max_length=255, unique=True, verbose_name='URL')),
            ],
            options={
                'verbose_name': 'Теги',
                'verbose_name_plural': 'Теги',
            },
        ),
    ]