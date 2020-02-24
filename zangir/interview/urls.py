from django.urls import include, path
from .views import QuestionView

urlpatterns = [
    path('', QuestionView.as_view())
    
]
