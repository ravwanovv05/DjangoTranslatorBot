from rest_framework import status
from rest_framework.generics import GenericAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from main.models.languages import Language
from main.serializers.languages import LanguageSerializer


class LanguageListAPIView(APIView):

    def get(self, request):
        languages = Language.objects.all()
        serializer = LanguageSerializer(languages, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class AddLanguageGenericAPIView(GenericAPIView):
    serializer_class = LanguageSerializer

    def get_object(self):
        return Language.objects.all()

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'success': True, 'message': 'Language added'}, status=status.HTTP_200_OK)
