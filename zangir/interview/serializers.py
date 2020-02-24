from rest_framework import serializers

from .models import Question, Option


class OptionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Option
        fields = ['id', 'text']


class QuestionSerializer(serializers.ModelSerializer):
    available_options = OptionSerializer(many=True)

    class Meta:
        model = Question
        fields = ['id', 'text', 'question_type', 'available_options']






        