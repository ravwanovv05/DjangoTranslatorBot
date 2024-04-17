from rest_framework import status
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from main.models.telegram_users import TelegramUser
from main.serializers.telegram_users import CreateTelegramUserSerializer
from main.utils.telegram_users import update_data_user


class CreateTelegramUserGenericAPIView(GenericAPIView):
    serializer_class = CreateTelegramUserSerializer

    def get_object(self):
        return TelegramUser.objects.all()

    def post(self, request, *args, **kwargs):
        first_name = request.data.get('first_name')
        last_name = request.data.get('last_name') if request.data.get('last_name') else None
        username = request.data.get('username') if request.data.get('username') else None
        language = request.data.get('language')
        telegram_id = request.data.get('telegram_id')
        update_data_user(first_name, language, telegram_id, username, last_name)

        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'success': True, 'message': 'Successfully created telegram user.'}, status=status.HTTP_201_CREATED)

