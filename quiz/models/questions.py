from django.db.models import (
    Model,
    CASCADE,
    CharField,
    TextField,
    ForeignKey,
)
from quiz.models.quiz import Quiz

class Question(Model):
    question = CharField(
        'вопрос',
        max_length=150,
    )
    full_text = TextField(
        'описание вопроса',
        blank=True,
    )
    quiz = ForeignKey(
        Quiz,
        on_delete=CASCADE,
        verbose_name='тест',
    )

    def __str__(self):
        return self.question[:40]

    class Meta:
        db_table = 'questions'
        verbose_name = 'вопрос'
        verbose_name_plural = 'вопросы'