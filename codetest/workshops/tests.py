from django.test import TestCase
from workshops.models import Workshop, Registration
from django.contrib.auth.models import User
from django.shortcuts import render_to_response,get_object_or_404
from django.core.management import call_command
import pdb
# Create your tests here.


class WorkshopTestClass(TestCase):
    def setUp(self):
        fixtures = ['./workshops/fixtures/my_initial_data']
        user1 = User.objects.create(username='johny2',password='password',email='johny@mail.com')
        user1.save()
        call_command("loaddata", "' + './workshops/fixtures/my_initial_data' + '",verbosity=0)


    def test_user_can_register(self):
        user1 = User.objects.get(username='johny2')
        #pdb.set_trace()
        workshop = get_object_or_404(Workshop, pk=1)
        reg = Registration.create(user=user1,workshop=workshop)
        self.assertEqual(True,user1 in workshop.members.all())
        self.assertEqual(True,workshop in user1.workshop_set.all())

    # def test_user_can_remove(self):
    #     user1=User.objects.get(username='johny2')
    #     workshop = Workshop.objects.get(pk=1)
    #     reg = Registration.create(user=user1,workshop=workshop)
    #     reg.save()
    #     reg.workshop = None
    #     reg.user = None
    #     reg.save()
    #     del reg
    #     self.assertEqual(True,workshop not in user1.workshop_set.all())
    #     self.assertEqual(True, user1 not in workshop.members.all())
    #
    #     #     if workshop_check == workshop:
    #     #         raise Exception("You already signed for this workshop")
    #     #     elif _overlap(workshop_check, workshop):
    #     #         raise Exception('Workshops can\'t overlap')
    #     # if not workshop.seats_left():
    #     #         raise Exception("Sorry,no seats left for this workshop.")
    #     #
    # def test_user_register_overlap(self):
    #     workshop_1 = Workshop.objects.get(pk=1)
    #     workshop_2 = Workshop.objects.get(pk=2)
    #     reg = Registration.create(user = user1,workshop = workshop_1)
    #     reg.save()
    #     self.assertRaises(Exception('Workshops can\'t overlap'),Registration.create(user=user1,workshop=workshop_2))
    #
    #
    # def test_user_register_twice(self):
    #     workshop_1 = Workshop.objects.get(pk=1)
    #     workshop_2 = Workshop.objects.get(pk=1)
    #     reg = Registration.create(user = user1,workshop = workshop_1)
    #     reg.save()
    #     self.assertRaises(Exception('You already signed for this workshop'),Registration.create(user=user1,workshop=workshop_2))
    #
    #
    # def test_user_no_seats_left(self):
    #
    #     for i in range(0,6):
    #          user[i] = User.objects.create(username='johny %s' %i,password='password',email='johny@mail.com')
    #          workshop_1 = Workshop.objects.get(pk=5)
    #
    #     reg = Registration.create(user = user1,workshop = workshop_1)
    #     reg.save()
    #     self.assertRaises(Exception('You already signed for this workshop'),Registration.create(user=user1,workshop=workshop_2))


#removing workshop that is not in your list

#
# def Test_register:
#
#     User.objects.create('johny1','password','johny@mail.com')
#     reg = Register.object.create(workshop=workshop, user=user)
#     contains workshop.members.all(workshop)
#     contains user.workshops.all(user)

# def testregistertwice():
#
#
# def testregisteroverlap()
#
# def Test_remove:
#     reg.user=none
#     reg.workshop = none
#     not contains workshop.members.all(workshop)
#     not contains user.workshops.all(user)
#
#
#
#
#
# def Seats()
#
#
# def TestNoLeftSeats()
#
#
