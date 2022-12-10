from django.db.models import (
    Model,
    CharField,
    TextField,
    SlugField,
    PositiveSmallIntegerField
)


class Category(Model):
    title = CharField(
        'название',
        max_length=100,
    )
    slug = SlugField(
        'URL',
        unique=True,
    )
    description = TextField(
        'описание', 
        blank=True,
    )
    sort = PositiveSmallIntegerField(
        'сортировка',
        default=0,
    )

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'categories'
        verbose_name = 'категория'
        verbose_name_plural = 'категории'

    
