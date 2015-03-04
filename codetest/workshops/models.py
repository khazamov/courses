from django.db import models
from django.contrib.auth.models import User

class Workshop(models.Model):

    title = models.CharField(max_length=100)
    tuition = models.PositiveIntegerField()
    capacity = models.PositiveIntegerField()
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    members=models.ManyToManyField(User, through='Registration', null=True)

    def seats_left(self):
        return self.capacity - len(self.members.all())

    def __unicode__(self):
        return self.title

#user1 = User.objects.create_user('omar',,'john@mail.ru','password')

class Registration(models.Model):
    user=models.ForeignKey(User)
    workshop = models.ForeignKey(Workshop, null=True)

    # def __init__(self):
    #     self.workshop.capacity =- 1
    #
