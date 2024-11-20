from django.test import TestCase
from users.models import User

class UserTest(TestCase):
    fixtures = ["user_sata.json"]
    
    def setUp(self):
        return super().setUp()
