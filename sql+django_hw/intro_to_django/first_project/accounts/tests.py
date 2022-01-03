from django.test import TestCase
from .models import MyUser

# Create your tests here.
class UserTestCase(TestCase):
  def setUp(self):
    MyUser.objects.create(user_name='Rudy451', password='password')

  def test_user_stuff(self):
    mine = MyUser.objects.get(user_name='Rudy451')
    self.assertEqual(mine.user_name, 'Rudy451')
    self.assertEqual(mine.password, 'password')
    self.assertTrue(len(mine.password) >= 6)
