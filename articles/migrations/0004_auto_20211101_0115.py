# Generated by Django 3.1.2 on 2021-10-31 18:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0003_auto_20211031_2231'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='articletags',
            options={'verbose_name': 'Тематика статьи', 'verbose_name_plural': 'Тематики статьи'},
        ),
        migrations.AddField(
            model_name='tags',
            name='articles',
            field=models.ManyToManyField(related_name='scopes', through='articles.ArticleTags', to='articles.Article'),
        ),
        migrations.AlterField(
            model_name='article',
            name='tags',
            field=models.ManyToManyField(through='articles.ArticleTags', to='articles.Tags', verbose_name='Тематики статьи'),
        ),
        migrations.AlterField(
            model_name='articletags',
            name='is_main',
            field=models.BooleanField(default=False, verbose_name='Основной'),
        ),
    ]