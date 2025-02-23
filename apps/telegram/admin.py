from django.contrib import admin
from apps.telegram.models import Telegram
# Register your models here.

@admin.register(Telegram)
class TelegramAdmin(admin.ModelAdmin):
    list_display = ('id', 'phone', 'persone', 'date', 'time')