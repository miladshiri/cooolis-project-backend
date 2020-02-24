from django.urls import include, path
from .views import QuestionView, QuestionnaireView, QuestionnaireDetailView

app_name = "interview"

urlpatterns = [
    path('', QuestionView.as_view()),
    path('questionnaire', QuestionnaireView.as_view()),
    path('questionnaire/<slug:slug>/', QuestionnaireDetailView.as_view(), name="questionnaire_detail"),
]
