from django.db import models
from django.contrib.auth.models import User

class Workshop(models.Model):
    title = models.CharField(max_length=100)
    tuition = models.PositiveIntegerField()
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    members=models.ManyToManyField(User, through='Registration', null=True)

    def __unicode__(self):
        return self.title



class Registration(models.Model):
    user=models.ForeignKey(User)
    workshop = models.ForeignKey(Workshop, null=True)
