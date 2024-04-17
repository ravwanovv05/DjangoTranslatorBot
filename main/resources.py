from import_export import resources
from main.models.statuses import Status
from main.models.languages import Language
from main.models.telegram_users import TelegramUser
from main.models.translate_languages import TranslateLanguage
from main.models.translates import Translate


class TelegramUserResource(resources.ModelResource):
    class Meta:
        model = TelegramUser


class LanguageResource(resources.ModelResource):
    class Meta:
        model = Language


class TranslateLanguageResource(resources.ModelResource):
    class Meta:
        model = TranslateLanguage


class StatusResource(resources.ModelResource):
    class Meta:
        model = Status


class TranslateResource(resources.ModelResource):
    class Meta:
        model = Translate
