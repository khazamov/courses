from django.test import TestCase
from models import Workshop, Registration
from django.contrib.auth.models import User
from django.core.management import call_command

# Create your tests here.


class WorkshopTestClass(TestCase):
    def setUp(self):
        User.object.create(username='johny2',password='password',email='johny@mail.com')
        Workshop.object.create()
        call_command("loaddata", "' + 'initial_data.json' + '",verbosity=0)


    def test_user_can_register(self):
        user1 = User.objects.get(username='johny2')
        workshop = Workshop.objects.get(pk=1)
        reg = Registration.objects.create(user=user1,workshop=workshop)
        self.assertEqual(True,user1 in workshop.members.all())
        self.assertEqual(True,workshop in user1.workshop_set.all())


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
