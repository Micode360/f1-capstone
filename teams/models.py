from django.db import models

# Create your models here.


class TeamModel(models.Model):
    name = models.CharField(max_length=200, blank=True)
    base = models.CharField(max_length=200, blank=True)
    team_principal = models.CharField(max_length=200, blank=True)
    championship_won = models.IntegerField(default=0, blank=True)
