from django.db import models


class Language(models.Model):
    name = models.CharField(max_length=30, unique=True, verbose_name='Name')
    lang_code = models.CharField(max_length=30, unique=True, verbose_name='Language code')

    class Meta:
        verbose_name = 'Language'
        verbose_name_plural = 'Languages'

    def __str__(self):
        return self.name
