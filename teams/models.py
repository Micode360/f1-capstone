from django.db import models

# Create your models here.


class TeamModel(models.Model):
    name = models.CharField(max_length=200)
    base = models.CharField(max_length=200)
    team_principal = models.CharField(max_length=200)
    championship_won = models.IntegerField(default=0)
