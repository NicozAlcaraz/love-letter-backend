from rest_framework import serializers
from .models import Letters

class LettersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Letters
        fields = "__all__"