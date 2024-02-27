from django.db import models
from django.contrib.auth.models import AbstractUser, User

# Create your models here.
"""https://www.jotform.com/form-templates/category/quiz-template"""

from django.db import models


class Quiz(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Quiz'
        verbose_name_plural = 'Quizzes'


class Question(models.Model):
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    title = models.TextField()

    @property
    def correct_answer(self, *args, **kwargs):
        try:
            data = Option.objects.get(question_id=self.id, is_correct=True)   
        except:
            data = False
        return data
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Question'
        verbose_name_plural = 'Questions'


class Option(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    name = models.TextField()
    is_correct = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        option = Option.objects.filter(question=self.question, is_correct=True)
        if option and self.is_correct:
            raise ValueError('Ikkita to`g`ri javob kiritish mumkin emas')
        elif not self.is_correct :
            raise ValueError('Birinchi to`g`ri javob kiriting ')
        super(Option, self).save(*args, **kwargs)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Option'
        verbose_name_plural = 'Options'


class Respondent(models.Model):
    full_name = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    email = models.EmailField(blank=True, null=True)
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)

    def __str__(self):
        return self.full_name
    
    class Meta:
        verbose_name = 'Respondent'
        verbose_name_plural = 'Respondents'

class Answer(models.Model):
    taker = models.ForeignKey(Respondent, on_delete=models.DO_NOTHING)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    answer = models.ForeignKey(Option, on_delete=models.CASCADE)
    is_correct = models.BooleanField()

    def __str__(self):
        return f"{self.taker.full_name} - {self.question.title}"
    
    class Meta:
        verbose_name = 'Answer'
        verbose_name_plural = 'Answers'

class Result(models.Model):
    taker = models.ForeignKey(Respondent, on_delete=models.CASCADE)
    correct_answers = models.IntegerField()
    incorrect_answers = models.IntegerField()

    @property
    def questions(self, *args, **kwargs):
        quiz = self.taker.quiz
        result = Question.objects.filter(quiz=quiz).count()
        return result
    
    @property
    def percentage(self, *args, **kwargs):
        return self.correct_answers / self.questions * 100
    
    def __str__(self):
        return f"{self.taker.full_name} - {self.percentage}%"
    
    class Meta:
        verbose_name = 'Result'
        verbose_name_plural = 'Results'