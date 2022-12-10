# Generated by Django 3.2.10 on 2022-12-10 00:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
        ('quiz', '0001_initial'),
    ]

    operations = [
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
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='account.account', verbose_name='автор')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='quiz.category', verbose_name='категория')),
            ],
            options={
                'verbose_name': 'тест',
                'verbose_name_plural': 'тесты',
                'db_table': 'quiz',
                'unique_together': {('slug', 'category')},
            },
        ),
    ]