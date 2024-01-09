from rest_framework import serializers
from .models import Keywords, Answers

class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answers
        fields = ['answer_text', 'audio_link']

class KeySerializer(serializers.ModelSerializer):
    answers = AnswerSerializer(many=True, read_only=True)

    class Meta:
        model = Keywords
        fields = "__all__"
