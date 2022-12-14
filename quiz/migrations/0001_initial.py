# Generated by Django 3.2.10 on 2022-12-14 22:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer', models.CharField(max_length=150, verbose_name='ответ')),
                ('is_correct', models.BooleanField(default=False, verbose_name='правильный ответ')),
            ],
            options={
                'verbose_name': 'ответ',
                'verbose_name_plural': 'ответы',
                'db_table': 'answers',
            },
        ),
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
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=150, verbose_name='вопрос')),
                ('full_text', models.TextField(blank=True, verbose_name='описание вопроса')),
            ],
            options={
                'verbose_name': 'вопрос',
                'verbose_name_plural': 'вопросы',
                'db_table': 'questions',
            },
        ),
        migrations.CreateModel(
            name='Quiz',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='название')),
                ('slug', models.SlugField(verbose_name='URL')),
                ('description', models.TextField(blank=True, verbose_name='описание')),
                ('is_public', models.BooleanField(default=True, verbose_name='отображается на стр. категории')),
                ('pub_date', models.DateTimeField(auto_now_add=True, verbose_name='создан')),
                ('mod_date', models.DateTimeField(auto_now=True, verbose_name='изменен')),
                ('sort', models.PositiveSmallIntegerField(default=0, verbose_name='сортировка')),
            ],
            options={
                'verbose_name': 'тест',
                'verbose_name_plural': 'тесты',
                'db_table': 'quiz',
            },
        ),
    ]
