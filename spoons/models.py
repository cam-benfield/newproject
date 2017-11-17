from django.db import models
from django.utils import timezone

class Day(models.Model):
    user = models.ForeignKey('auth.User')
    spoonstart = models.IntegerField(
        default = 20)
    spoonsnow = models.IntegerField(
        default = 20)
    notes = models.TextField()

    def usespoons(self):
        print("How many spoons have you used?")
        spoonsused = input('>')
        self.spoonsnow = spoonsnow-spoonsused
        self.save()
