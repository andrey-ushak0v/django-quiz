from django.db.models import (CASCADE, BooleanField, CharField, ForeignKey,
                              Model,)

from quiz.models.questions import Question


class Answer(Model):
    answer = CharField(
        'ответ',
        max_length=150,
    )
    is_correct = BooleanField(
        'правильный ответ',
        default=False,
    )
    question = ForeignKey(
        Question,
        on_delete=CASCADE,
        verbose_name='вопрос'
    )

    def __str__(self):
        return self.answer

    class Meta:
        db_table = 'answers'
        verbose_name = 'ответ'
        verbose_name_plural = 'ответы'
