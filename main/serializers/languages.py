from rest_framework import serializers
from main.models.languages import Language


class LanguageSerializer(serializers.ModelSerializer):

    class Meta:
        model = Language
        fields = '__all__'
