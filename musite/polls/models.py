from django.db import models

# Create your models here.
'''
Question
1)Question_Text 2)publishDate
Choice
1)Choice_Text 2)no_Of_votes 3) link of choices to question

'''
class Question(models.Model):     #let django know that class question is of type model
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.question_text

class Choice(models.Model):
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)

    def __str__(self):
        return self.choice_text

