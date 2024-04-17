from rest_framework import status
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from django.db.models import Q
from main.models.languages import Language
from main.models.telegram_users import TelegramUser
from main.models.translate_languages import TranslateLanguage
from main.models.translates import Translate
from main.serializers.languages import LanguageSerializer
from main.serializers.translates import SetLanguageSerializer, TranslateSerializer
from main.utils.translator import translate_message


class SetLanguageGenericAPIView(GenericAPIView):
    serializer_class = SetLanguageSerializer

    def get_object(self):
        return TranslateLanguage.objects.all()

    def post(self, request, *args, **kwargs):
        language = Language.objects.filter(pk=request.data.get('language')).first()
        telegram_id = request.data.get('telegram_id')

        if TranslateLanguage.objects.filter(telegram_id=telegram_id).exists():
            translate_language = TranslateLanguage.objects.get(Q(telegram_id=telegram_id))
            translate_language.language = language
            translate_language.save()
        else:
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
        return Response({'status': True, 'message': 'Successfully had set.'}, status=status.HTTP_200_OK)


class SelectedLanguageGenericAPIView(GenericAPIView):
    serializer_class = LanguageSerializer

    def get(self, request, telegram_id, *args, **kwargs):
        selected_language = TranslateLanguage.objects.filter(telegram_id=telegram_id).first().language.id
        language_data = Language.objects.filter(pk=selected_language).first()
        serializer = self.get_serializer(language_data)
        return Response(serializer.data)


class TranslateMessageGenericAPIView(GenericAPIView):
    serializer_class = TranslateSerializer

    def post(self, request, *args, **kwargs):
        text = request.data.get('text')
        telegram_id = request.data.get('telegram_id')
        telegram_user = TelegramUser.objects.filter(telegram_id=telegram_id).first()
        data = {}
        if TranslateLanguage.objects.filter(telegram_id=telegram_id).exists():
            if Translate.objects.filter(telegram_id=telegram_id).exists():
                translate = Translate.objects.get(Q(telegram_id=telegram_id))
                dest = TranslateLanguage.objects.filter(telegram_user=telegram_user).first().language.lang_code
                translated_text = translate_message(text, dest)
                translate.text = text
                translate.translated_text = translated_text
                translate.save()
                data['translated_text'] = translated_text
            else:
                serializer = self.get_serializer(data=request.data)
                serializer.is_valid(raise_exception=True)
                serializer.save()
                data['translated_text'] = serializer.data['translated_text']
        return Response(data)

