from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import mixins, generics

from .serializers import QuestionSerializer
from .models import Question


class QuestionView(mixins.ListModelMixin,
                    generics.GenericAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    
    
