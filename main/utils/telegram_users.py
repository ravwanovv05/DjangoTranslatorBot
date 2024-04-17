from main.models.telegram_users import TelegramUser
from django.db.models import Q


def update_data_user(first_name, language, telegram_id, username=None, last_name=None):
    first_name = first_name
    last_name = last_name
    username = username
    language = language
    telegram_id = telegram_id

    try:
        telegram_user = TelegramUser.objects.get(Q(telegram_id=telegram_id))
        telegram_user.first_name = first_name
        telegram_user.last_name = last_name
        telegram_user.username = username
        telegram_user.language = language
        telegram_user.save()
    except TelegramUser.DoesNotExist:
        return False

    return telegram_user
