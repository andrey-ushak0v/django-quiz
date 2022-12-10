from django.contrib.admin import (
    ModelAdmin,
    register,
)
from quiz.models.quiz import Quiz


@register(Quiz)
class QuizModelAdmin(ModelAdmin):
    prepopulated_fields = {
        'slug': ('title',)
    }