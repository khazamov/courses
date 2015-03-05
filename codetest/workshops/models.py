from django.db import models
from django.contrib.auth.models import User




class Workshop(models.Model):

    title = models.CharField(max_length=100)
    tuition = models.PositiveIntegerField()
    capacity = models.PositiveIntegerField()
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    members=models.ManyToManyField(User, through='Registration', null=True)

    #added capacity
    #more tuition - less capacity
    def seats_left(self):
        return self.capacity - len(self.members.all())

    #to be displayed on front page
    def duration(self):
        return self.end_time - self.start_time

    def __unicode__(self):
        return self.title


def _overlap(ws1, ws2):
    latest_start = max(ws1.start_time, ws2.start_time)
    earliest_end = min(ws1.end_time, ws2.end_time)
    return latest_start <= earliest_end



class Registration(models.Model):
    user=models.ForeignKey(User)
    workshop = models.ForeignKey(Workshop, null=True)

    @classmethod
    def create(cls, user, workshop):
        for workshop_check in user.workshop_set.all():
            if workshop_check == workshop:
                raise Exception("You already signed for this workshop")
            elif _overlap(workshop_check, workshop):
                raise Exception('Workshops can\'t overlap')
        if not workshop.seats_left():
                raise Exception("Sorry,no seats left for this workshop.")
        reg=cls(user=user,workshop=workshop)
        return reg

