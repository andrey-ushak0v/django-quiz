from django.contrib.admin import ModelAdmin, register

from user.models import Account


@register(Account)
class UserModelAdmin(ModelAdmin):
    pass
