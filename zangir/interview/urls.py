from django.urls import include, path
from . import views

app_name = "interview"

urlpatterns = [
    path('', views.QuestionView.as_view()),
    path('questionnaire/', views.QuestionnaireView.as_view()),
    path('categories/', views.CategoryView.as_view()),
    path('questionnaire/<int:pk>/', views.QuestionnaireDetailView.as_view(), name="questionnaire_detail"),
    path('sendanswers/', views.GetAnswersView.as_view()),
]
