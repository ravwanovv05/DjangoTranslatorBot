from django.db import models


class TelegramUser(models.Model):
    first_name = models.CharField(max_length=200, verbose_name='First name')
    last_name = models.CharField(max_length=200, null=True, blank=True, verbose_name='Last name')
    username = models.CharField(max_length=200, null=True, blank=True, unique=True, verbose_name='Username')
    telegram_id = models.PositiveIntegerField(unique=True, verbose_name='Telegram ID')
    language = models.CharField(max_length=10, verbose_name='Language')
    joined_at = models.DateTimeField(auto_now_add=True, null=True, blank=True, verbose_name='Joined at')

    class Meta:
        verbose_name = 'Telegram user'
        verbose_name_plural = 'Telegram users'

    def __str__(self):
        return f'{self.first_name}'
