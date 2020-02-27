from django.contrib import admin
from .models import Area, Question, Option, Questionnaire, Category

admin.site.register(Area)
admin.site.register(Question)
admin.site.register(Option)
admin.site.register(Questionnaire)
admin.site.register(Category)
