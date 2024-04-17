from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from main.models.statuses import Status
from main.models.languages import Language
from main.models.telegram_users import TelegramUser
from main.models.translate_languages import TranslateLanguage
from main.models.translates import Translate
from main.resources import TelegramUserResource, LanguageResource, TranslateLanguageResource, StatusResource, TranslateResource


@admin.register(TelegramUser)
class TelegramUserAdmin(ImportExportModelAdmin):
    list_display = ('first_name', 'last_name', 'username', 'joined_at')
    list_display_links = ('first_name',)
    search_fields = ('first_name', 'last_name', 'username')
    list_per_page = 10
    resource_class = TelegramUserResource


@admin.register(Language)
class LanguageAdmin(ImportExportModelAdmin):
    list_display = ('name', 'lang_code')
    list_display_links = ('name',)
    search_fields = ('name',)
    list_per_page = 10
    resource_class = LanguageResource


@admin.register(TranslateLanguage)
class TranslateLanguageAdmin(ImportExportModelAdmin):
    list_display = ('language', 'telegram_user')
    list_display_links = ('language',)
    search_fields = ('language',)
    list_per_page = 10
    resource_class = TranslateLanguageResource


@admin.register(Status)
class StatusAdmin(ImportExportModelAdmin):
    list_display = ('first_name', 'last_name', 'conclusion')
    list_display_links = ('first_name',)
    search_fields = ('first_name', 'last_name')
    list_per_page = 10
    resource_class = StatusResource


@admin.register(Translate)
class TranslateAdmin(ImportExportModelAdmin):
    list_display = ('id', 'text', 'translated_text',)
    list_display_links = ('id',)
    search_fields = ('telegram_user',)
    list_per_page = 10
    resource_class = TranslateResource
