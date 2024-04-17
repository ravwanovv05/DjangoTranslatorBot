from rest_framework import serializers
from main.models.telegram_users import TelegramUser


class CreateTelegramUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = TelegramUser
        fields = '__all__'

    def validate(self, attrs):
        telegram_id = attrs['telegram_id']

        if TelegramUser.objects.filter(telegram_id=telegram_id).exists():
            raise serializers.ValidationError('Telegram user already exists!')

        return attrs
