from django.urls import include, path
from .views import QuestionView, QuestionnaireView, QuestionnaireDetailView

urlpatterns = [
    path('', QuestionView.as_view()),
    path('questionnaire', QuestionnaireView.as_view()),
    path('questionnaire/<slug:slug>/', QuestionnaireDetailView.as_view()),
]
