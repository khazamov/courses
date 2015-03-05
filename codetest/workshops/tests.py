from django.test import TestCase
from workshops.models import Workshop, Registration,_overlap
from django.contrib.auth.models import User
from django.shortcuts import render_to_response,get_object_or_404
import pdb

#earliest end - latest start
# def _overlap(ws1, ws2):
#     latest_start = max(ws1.start_time, ws2.start_time)
#     earliest_end = min(ws1.end_time, ws2.end_time)
#     return latest_start <= earliest_end
#


class WorkshopTestClass(TestCase):

    fixtures = ['workshops/fixtures/my_initial_data.json']

    def setUp(self):
        self.user1 = User.objects.create(username='johny',password='password',email='johny@mail.com')
        self.user1.save()


    def test_user_can_register(self):
        user1 = User.objects.get(username='johny')
        #pdb.set_trace()
        workshop = get_object_or_404(Workshop, pk=1)
        reg = Registration.create(user=user1,workshop=workshop)
        reg.save()
        self.assertEqual(True,user1 in workshop.members.all())
        self.assertEqual(True,workshop in user1.workshop_set.all())

    def test_user_can_remove(self):
        user1=User.objects.get(username='johny')
        workshop = Workshop.objects.get(pk=1)
        reg = Registration.create(user=user1,workshop=workshop)
        reg.save()
        reg.workshop = None
        reg.save()
        del reg
        self.assertEqual(True,workshop not in user1.workshop_set.all())
        self.assertEqual(True, user1 not in workshop.members.all())

#positive and negative tests. pulling test cases based on ID

    def test_user_register_donot_overlap(self):
       try:
        workshop_1 = Workshop.objects.get(pk=2)
        workshop_2 = Workshop.objects.get(pk=3)
        #pdb.set_trace()
        reg = Registration.create(user = self.user1, workshop = workshop_1)
        reg.save()
        Registration.create(self.user1,workshop_2)
       except Exception, Msg:
           raise "Exception was raised for non-overlapping workshops"

    def test_user_register_overlap_same_day(self):
        workshop_1 = Workshop.objects.get(pk=5)
        workshop_2 = Workshop.objects.get(pk=6)
        reg = Registration.create(user = self.user1, workshop = workshop_1)
        reg.save()
        with self.assertRaisesMessage(Exception, "Workshops can't overlap"):
            Registration.create(self.user1,workshop_2)

    def test_user_register_overlap_different_days(self):
        workshop_1 = Workshop.objects.get(pk=4)
        workshop_2 = Workshop.objects.get(pk=5)
        reg = Registration.create(user = self.user1, workshop = workshop_1)
        reg.save()
        with self.assertRaisesMessage(Exception, "Workshops can't overlap"):
            Registration.create(self.user1,workshop_2)




    def test_user_register_twice(self):
        workshop_1 = Workshop.objects.get(pk=1)
        workshop_2 = Workshop.objects.get(pk=1)
        reg = Registration.create(user = self.user1,workshop = workshop_1)
        reg.save()
        with self.assertRaisesMessage(Exception, "You already signed for this workshop"):
            Registration.create(self.user1,workshop_2)

    def test_user_no_seats_left(self):

        workshop_1 = Workshop.objects.get(pk=5)
        for i in range(0,10):
             user = User.objects.create(username='johny %s' %i,password='password',email='johny@mail.com')
             reg = Registration.create(user = user, workshop = workshop_1)
             reg.save()
        with self.assertRaisesMessage(Exception, "Sorry,no seats left for this workshop."):
            Registration.create(self.user1,workshop_1)


