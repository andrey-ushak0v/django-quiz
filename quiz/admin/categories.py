from django.contrib.admin import ModelAdmin, register

from quiz.models.categories import Category


@register(Category)
class CategoryModelAdmin(ModelAdmin):
    prepopulated_fields = {
        'slug': ('title',)
    }
