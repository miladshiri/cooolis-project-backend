from django.db import models


class ZangirBaseModel(models.Model):
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)
    
    class Meta:
        abstract = True

class Question(ZangirBaseModel):
    ONE_ANSWER = 'OA'
    MULTIPLE_ANSWER = 'MA'

    QUESTION_TYPES = [
        (ONE_ANSWER, 'one_answer'),
        (MULTIPLE_ANSWER, 'multiple_answer')
    ]

    question = models.TextField(max_length=200)
    qtype = models.TextField(choices=QUESTION_TYPES)


