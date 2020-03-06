from django.contrib import admin
from .models import Area, Question, Option, Questionnaire, Category

class OptionsInLine(admin.TabularInline):
    model = Option
    extra = 0

@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
 
    # list_display = ("text", "question", "is_answer")
  
    inlines = [
        OptionsInLine
    ]


admin.site.register(Area)
# admin.site.register(Question)
admin.site.register(Option)
admin.site.register(Questionnaire)
admin.site.register(Category)

