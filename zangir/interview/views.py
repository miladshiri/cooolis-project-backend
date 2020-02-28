from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import mixins, generics

from .serializers import QuestionSerializer, QuestionnaireSerializer, \
QuestionnaireListSerializer, CategoryListSerializer
from .models import Question, Questionnaire, Category
from rest_framework.permissions import IsAuthenticated


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

class CategoryView(mixins.ListModelMixin, generics.GenericAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Category.objects.all()
    serializer_class = CategoryListSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class QuestionnaireDetailView(mixins.RetrieveModelMixin,
                    generics.GenericAPIView):
    queryset = Questionnaire.objects.all()
    serializer_class = QuestionnaireSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    
    

    
    

    
