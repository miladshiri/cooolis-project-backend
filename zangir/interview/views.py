from django.shortcuts import render
from django.shortcuts import get_object_or_404

from rest_framework.views import APIView
from rest_framework import mixins, generics
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework import status


from .serializers import QuestionSerializer, QuestionnaireSerializer, \
QuestionnaireListSerializer, CategoryListSerializer, ResponseSerializer
from .models import Question, Questionnaire, Category


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
    # permission_classes = (AllowAny,)
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


from django.views.decorators.csrf import csrf_protect
from django.utils.decorators import method_decorator

class GetAnswersView(APIView):
    permission_classes = [AllowAny,]

    def post(self, request):
        print (request.data)
        serializer = ResponseSerializer(data=request.data, many=True)
        if serializer.is_valid():
            total_questions = len(serializer.data)
            full_score = 0
            result_score = 0
            for question in serializer.data:
                question_object = get_object_or_404(Question, id=question['question_id'])
                selected_options = question['selected_options']
                full_score += question_object.complexity
                
                if question_object.question_type == Question.ONE_ANSWER_TYPE:
                    if len(selected_options) == 1:
                        selected_option = selected_options[0]
                        right_answer = question_object.answers()[0]
                        if selected_option['id'] == right_answer.id:
                            result_score += question_object.complexity

                elif question_object.question_type == Question.MULTIPLE_ANSWER_TYPE:
                    answers_id = list(question_object.answers().values_list('id', flat=True))
                    partial_score = question_object.complexity / len(answers_id)
                    for selected_option in selected_options:
                        if selected_option['id'] in answers_id:
                            result_score += partial_score
                else:
                    print ('unkinw')

            print (full_score)
            final_score = result_score/full_score*100
            return Response({'score':final_score}, status=status.HTTP_200_OK)
        else:
            return Response('format is not correct', status=status.HTTP_200_OK)

    
