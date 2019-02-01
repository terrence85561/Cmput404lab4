from django.db import models
import datetime
from django.utils import timezone
# Create your models here.

# Question has a question and a publication date
# Choice has two fields: the text of the choice and a vote tally.

# Each model is a Python class that subclasses django.db.models.Model
# Each attribute of the model represents a database field.
# With all of this,Django gives you an automatically-generated database-access API;
#   see:https://docs.djangoproject.com/en/2.1/topics/db/queries/.


class Question(models.Model):
    # 继承models.Model
    # CharField stands for character field
    # xxxField relates to a column in database

    question_text = models.CharField(max_length=200)

    # publish date
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text
