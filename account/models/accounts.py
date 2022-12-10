from django.db.models import (
    SET_NULL,
    OneToOneField,
    CharField,
    BooleanField,
    Model,
)
from django.contrib.auth.models import User

class Account(Model):
    login = OneToOneField(
        User, 
        null=True,
        on_delete=SET_NULL,
        verbose_name='логин',
    )
    first_name = CharField(
        'имя',
        max_length=50,
    )
    last_name = CharField(
        'фамилия',
        max_length=50,
    )
    can_create = BooleanField(
        'может создавать тесты'
    )
    
    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    class Meta:
        db_table = 'accounts'
        verbose_name = 'аккаунт'
        verbose_name_plural = 'аккаунты'
