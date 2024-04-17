from django.db import models
from main.models.telegram_users import TelegramUser


class Translate(models.Model):
    text = models.TextField('Text')
    translated_text = models.TextField('Translated text')
    telegram_user = models.ForeignKey(TelegramUser, on_delete=models.CASCADE, verbose_name='Telegram user')
    telegram_id = models.PositiveIntegerField(unique=True, verbose_name='Telegram ID')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Created at')

    class Meta:
        verbose_name = 'Translate'
        verbose_name_plural = 'Translates'

    def __str__(self):
        return f"{self.pk}"


