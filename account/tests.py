from django.test import TestCase
from .models import User

# Create your tests here.
class AccountTestCase(TestCase):

    def setUp(self):
        a1 = User.objects.create(email="john@doe.co", alias="johndoe", password="aQ1!aQ1!")
        a2 = User.objects.create(email="john@doe.c", alias="johndoe2", password="aQ1!aQ1!")
        a3 = User.objects.create(email=".john@doe.c", alias="johndoe", password="aQ1!aQ1!")
        a3 = User.objects.create(email="john@doe.co", alias="johndoe", password="aQ1!aQ1!")

    def test_userCreation(self):
        
        self.assertContains()