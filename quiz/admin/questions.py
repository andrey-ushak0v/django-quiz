from django.contrib.admin import (
    ModelAdmin,
    register,
)
from quiz.models.questions import Question
from quiz.admin.answers import AnswerTabularInline


@register(Question)
class QuestionModelAdmin(ModelAdmin):
    inlines=(
        AnswerTabularInline,
    )
