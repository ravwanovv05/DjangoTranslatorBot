from django.db import models


class Status(models.Model):
    first_name = models.CharField(max_length=200, verbose_name='First name')
    last_name = models.CharField(max_length=200, null=True, blank=True, verbose_name='Last name')
    username = models.CharField(max_length=200, null=True, blank=True, verbose_name='Username')
    conclusion = models.CharField(max_length=5, verbose_name='Conclusion')
    telegram_id = models.PositiveBigIntegerField(unique=True, verbose_name='Telegram ID')

    class Meta:
        verbose_name = 'Status'
        verbose_name_plural = 'Statuses'

    def __str__(self):
        return self.first_name
