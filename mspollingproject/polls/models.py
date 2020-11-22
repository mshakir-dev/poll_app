from django.db import models

class Question(models.Model):
  question_text = models.CharField(max_length=30)
  pub_date = models.DateTimeField('date published')
  description_poll = models.CharField(max_length=100)
  
  # This method will display question_text in the Admin instead object
  def __str__(self):
    return self.question_text

class Choice(models.Model):
  # question field is making a relation with the Question MODEL by assigning the foriegnKey
  question = models.ForeignKey(Question, on_delete=models.CASCADE)
  choice_text = models.CharField(max_length=200)
  votes = models.IntegerField(default=10)

  def __str__(self):
    return self.choice_text