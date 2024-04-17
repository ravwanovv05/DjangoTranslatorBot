from rest_framework import serializers
from main.models.languages import Language
from main.models.telegram_users import TelegramUser
from main.models.translate_languages import TranslateLanguage
from main.models.translates import Translate
from main.utils.translator import translate_message


class SetLanguageSerializer(serializers.ModelSerializer):

    class Meta:
        model = TranslateLanguage
        fields = '__all__'
        read_only_fields = ('telegram_user',)

    def create(self, validated_data):
        telegram_id = validated_data['telegram_id']
        telegram_user = TelegramUser.objects.filter(telegram_id=telegram_id).first()
        return TranslateLanguage.objects.create(telegram_user=telegram_user, **validated_data)


class TranslateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Translate
        fields = '__all__'
        read_only_fields = ('translated_text', 'telegram_user')

    def validate(self, attrs):
        telegram_id = attrs.get('telegram_id')

        if not TranslateLanguage.objects.filter(telegram_id=telegram_id).exists():
            raise serializers.ValidationError('You were not chosen a language.')
        return attrs

    def create(self, validated_data):
        text = validated_data['text']
        telegram_id = validated_data['telegram_id']
        telegram_user = TelegramUser.objects.filter(telegram_id=telegram_id).first()
        dest = TranslateLanguage.objects.filter(telegram_user=telegram_user).first().language.lang_code
        translated_text = translate_message(text, dest)
        translate_instance = Translate.objects.create(telegram_user=telegram_user, translated_text=translated_text, **validated_data)
        return translate_instance
