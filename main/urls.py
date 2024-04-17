from django.urls import path
from main.views.languages import LanguageListAPIView, AddLanguageGenericAPIView
from main.views.telegram_users import CreateTelegramUserGenericAPIView
from main.views.translates import SetLanguageGenericAPIView, SelectedLanguageGenericAPIView, \
    TranslateMessageGenericAPIView

urlpatterns = [
    path('create-telegram-user', CreateTelegramUserGenericAPIView.as_view(), name='create_telegram_user'),
    path('set-language', SetLanguageGenericAPIView.as_view(), name='set_language'),
    path('language-list', LanguageListAPIView.as_view(), name='language_list'),
    path('add-language', AddLanguageGenericAPIView.as_view(), name='add_language'),
    path('selected-language/<int:telegram_id>', SelectedLanguageGenericAPIView.as_view(), name='selected_language'),
    path('translate-message', TranslateMessageGenericAPIView.as_view(), name='translate_message'),

]
