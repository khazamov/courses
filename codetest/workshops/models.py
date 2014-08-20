from django.db import models


class Workshop(models.Model):
    title = models.CharField(max_length=100)
    tuition = models.PositiveIntegerField()
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    
    def __unicode__(self):
        return self.title
