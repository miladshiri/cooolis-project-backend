from rest_framework import serializers

from .models import Question, Option, Questionnaire, Category


class OptionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Option
        fields = ['id', 'text']


class QuestionSerializer(serializers.ModelSerializer):
    available_options = OptionSerializer(many=True)

    class Meta:
        model = Question
        fields = ['id', 'text', 'question_type', 'available_options']


class QuestionnaireListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Questionnaire
        fields = ['id', 'title', 'slug', 'description', 'max_number', 'get_absolute_url']


class CategoryListSerializer(serializers.ModelSerializer):
    all_questionnaires = QuestionnaireListSerializer(many=True)

    class Meta:
        model = Category
        fields = ['text', 'all_questionnaires']


class QuestionnaireSerializer(serializers.ModelSerializer):
    questions = QuestionSerializer(many=True)

    class Meta:
        model = Questionnaire
        fields = ['title', 'slug', 'description', 'max_number', 'questions']



        