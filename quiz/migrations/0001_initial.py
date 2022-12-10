# Generated by Django 3.2.10 on 2022-12-09 23:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='название')),
                ('slug', models.SlugField(unique=True, verbose_name='URL')),
                ('description', models.TextField(blank=True, verbose_name='описание')),
                ('sort', models.PositiveSmallIntegerField(default=0, verbose_name='сортировка')),
            ],
            options={
                'verbose_name': 'категория',
                'verbose_name_plural': 'категории',
                'db_table': 'categories',
            },
        ),
    ]
