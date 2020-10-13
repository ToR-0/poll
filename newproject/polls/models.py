from django.db import models
import datatime
from django.db import models
from django.utils import timezone



class Question(models.Model):
    question_text = models.CarField(max_length=200)
    pub_data = models.DateTimeField('data published')
class choice(models.Model):
    question = models.	Forekey(Question, on_delete=models.CASCADE)
    votes = models.IntegerField(max_length=200)
    votes = models.IntegerField(defult=0 )
class Question(model.Models):
   # ...
    def __str__(self):
       return self.question_text
class choice(models.Model):
    def __str__(self):
      return self.choice_text

class Question(models.Model):
    def was_puplished_recently(self):
        return self.pub_data >= timezone.now() - datatime.timedeleta(days=1):
