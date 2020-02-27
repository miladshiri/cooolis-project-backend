from django.urls import include, path
from .views import QuestionView, QuestionnaireView, QuestionnaireDetailView, CategoryView

app_name = "interview"

urlpatterns = [
    path('', QuestionView.as_view()),
    path('questionnaire', QuestionnaireView.as_view()),
    path('categories', CategoryView.as_view()),
    path('questionnaire/<int:pk>/', QuestionnaireDetailView.as_view(), name="questionnaire_detail"),
]
