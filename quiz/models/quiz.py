from django.db.models import (
    Model,
    PROTECT,
    CharField,
    TextField,
    SlugField,
    BooleanField,
    ForeignKey,
    DateTimeField,
    PositiveSmallIntegerField
)
from django.urls import reverse

from account.models.accounts import Account
from quiz.models.categories import Category

class Quiz(Model):
    author = ForeignKey(
        Account,
        on_delete=PROTECT,
        verbose_name='автор'
    )
    title = CharField(
        'название',
        max_length=100,
    )
    slug = SlugField(
        'URL',
        unique=False,
    )
    description = TextField(
        'описание',
        blank=True,
    )
    is_public = BooleanField(
        'отображается на стр. категории',
        default=True,
    )
    category = ForeignKey(
        Category,
        on_delete=PROTECT,
        verbose_name='категория',

    )
    pub_date = DateTimeField(
        'создан',
        auto_now_add=True,
    )
    mod_date = DateTimeField(
        'изменен',
        auto_now=True
    )        
    sort = PositiveSmallIntegerField(
        'сортировка',
        default=0,
    )

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'quiz'
        verbose_name = 'тест'
        verbose_name_plural = 'тесты'
        unique_together = (
            'slug',
            'category',
        )

    def get_absolute_url(self):
        return reverse(
            'quiz',
            kwargs={
                'quiz_slug': self.slug,
                'category_slug': self.category.slug,
            }
        )

    
