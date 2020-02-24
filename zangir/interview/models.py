from django.db import models


class ZangirBaseModel(models.Model):
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)
    
    class Meta:
        abstract = True


class Area(ZangirBaseModel):
    text = models.CharField(max_length=100)


    def __str__(self):
        return self.text[:20]



class Question(ZangirBaseModel):
    UNKNOWN_TYPE = 'UT'
    ONE_ANSWER_TYPE = 'OA'
    MULTIPLE_ANSWER_TYPE = 'MA'
    EMPTY_SPACE_TYPE = 'ES'

    text = models.TextField()
    complexity = models.IntegerField(default=2)
    areas = models.ManyToManyField(Area)


    def __str__(self):
        return self.text[:20]

    @property
    def question_type(self):
        answer_num = self.option_set.filter(is_answer=True).count()
        options_num = self.option_set.count()

        if answer_num == 1 and options_num == 1:
            return self.EMPTY_SPACE_TYPE
        elif answer_num == 1 and options_num > 1:
            return self.ONE_ANSWER_TYPE
        elif answer_num > 1:
            return self.MULTIPLE_ANSWER_TYPE
        else:
            return self.UNKNOWN_TYPE


    def answers(self):
        return self.option_set.filter(is_answer=True)

    def available_options(self):
        return self.option_set.all() if not self.question_type == 'ES' else Option.objects.none()

class Option(ZangirBaseModel):
    text = models.TextField()
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    is_answer = models.BooleanField(default=False)

    def __str__(self):
        return self.text[:20]


class Questionnaire(ZangirBaseModel):
    title = models.CharField(max_length=100)
    description = models.TextField()
    target_areas = models.ManyToManyField(Area)
    max_number = models.IntegerField()


    def __str__(self):
        return self.title

    def questions(self):
        return Question.objects.filter(areas__in=self.target_areas.all())[:self.max_number]

