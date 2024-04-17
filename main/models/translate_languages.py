from django.db import models
from main.models.languages import Language
from main.models.telegram_users import TelegramUser


class TranslateLanguage(models.Model):
    language = models.ForeignKey(Language, on_delete=models.CASCADE, verbose_name='Language ID')
    telegram_id = models.PositiveIntegerField(unique=True, verbose_name='Telegram ID')
    telegram_user = models.ForeignKey(TelegramUser, on_delete=models.CASCADE, verbose_name='Telegram User')

    class Meta:
        verbose_name = 'Translate Language'
        verbose_name_plural = 'Translate Languages'

    def __str__(self):
        return self.language.name

