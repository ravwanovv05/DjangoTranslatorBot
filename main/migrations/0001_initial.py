# Generated by Django 5.0.3 on 2024-04-15 18:37

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Language',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, unique=True, verbose_name='Name')),
                ('lang_code', models.CharField(max_length=30, unique=True, verbose_name='Language code')),
            ],
            options={
                'verbose_name': 'Language',
                'verbose_name_plural': 'Languages',
            },
        ),
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=200, verbose_name='First name')),
                ('last_name', models.CharField(blank=True, max_length=200, null=True, verbose_name='Last name')),
                ('username', models.CharField(blank=True, max_length=200, null=True, verbose_name='Username')),
                ('conclusion', models.CharField(max_length=5, verbose_name='Conclusion')),
                ('telegram_id', models.PositiveBigIntegerField(unique=True, verbose_name='Telegram ID')),
            ],
            options={
                'verbose_name': 'Status',
                'verbose_name_plural': 'Statuses',
            },
        ),
        migrations.CreateModel(
            name='TelegramUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=200, verbose_name='First name')),
                ('last_name', models.CharField(blank=True, max_length=200, null=True, verbose_name='Last name')),
                ('username', models.CharField(blank=True, max_length=200, null=True, unique=True, verbose_name='Username')),
                ('telegram_id', models.PositiveIntegerField(unique=True, verbose_name='Telegram ID')),
                ('language', models.CharField(max_length=10, verbose_name='Language')),
                ('joined_at', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Joined at')),
            ],
            options={
                'verbose_name': 'Telegram user',
                'verbose_name_plural': 'Telegram users',
            },
        ),
        migrations.CreateModel(
            name='Translate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(verbose_name='Text')),
                ('translated_text', models.TextField(verbose_name='Translated text')),
                ('telegram_id', models.PositiveIntegerField(unique=True, verbose_name='Telegram ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
                ('telegram_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.telegramuser', verbose_name='Telegram user')),
            ],
            options={
                'verbose_name': 'Translate',
                'verbose_name_plural': 'Translates',
            },
        ),
        migrations.CreateModel(
            name='TranslateLanguage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('telegram_id', models.PositiveIntegerField(unique=True, verbose_name='Telegram ID')),
                ('language', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.language', verbose_name='Language ID')),
                ('telegram_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.telegramuser', verbose_name='Telegram User')),
            ],
            options={
                'verbose_name': 'Translate Language',
                'verbose_name_plural': 'Translate Languages',
            },
        ),
    ]
