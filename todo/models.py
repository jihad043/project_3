from django.db import models

class Todo(models.Model):
    class AgeChoices(models.IntegerChoices):
        YOUNG = 1, 'Young'
        ADULT = 2, 'Adult'
        OLD = 3, 'Old'

    name = models.CharField(max_length=100)
    age = models.IntegerField(choices=AgeChoices.choices)
    address = models.TextField()
