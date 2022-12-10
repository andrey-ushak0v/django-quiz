from django.contrib.admin import register, ModelAdmin
from account.models import Account

@register(Account)
class AccountModelAdmin(ModelAdmin):
    pass
