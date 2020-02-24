from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import mixins, generics

from .serializers import QuestionSerializer, QuestionnaireSerializer, QuestionnaireListSerializer
from .models import Question, Questionnaire


class QuestionView(mixins.ListModelMixin,
                    generics.GenericAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class QuestionnaireView(mixins.ListModelMixin,
                    generics.GenericAPIView):
    queryset = Questionnaire.objects.all()
    serializer_class = QuestionnaireListSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class QuestionnaireDetailView(mixins.RetrieveModelMixin,
                    generics.GenericAPIView):
    queryset = Questionnaire.objects.all()
    serializer_class = QuestionnaireSerializer
    lookup_field = "slug"

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    
    

    
    

    
