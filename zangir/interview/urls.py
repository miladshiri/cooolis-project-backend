from django.urls import include, path
from .views import QuestionView, QuestionnaireView

urlpatterns = [
    path('', QuestionView.as_view()),
    path('questionnaire', QuestionnaireView.as_view())
]
