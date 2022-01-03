from django.test import TestCase
from django.urls import reverse

# Create your tests here.
class RoutingTests(TestCase):
  def setUp(self):
    pass

  def test_home_url(self):
    url = reverse('home')
    self.response = self.client.get(url)
    self.assertEqual(self.response.status_code, 200)

  def test_kitchen_url(self):
    url = reverse('kitchen')
    self.response = self.client.get(url)
    self.assertEqual(self.response.status_code, 200)

  def test_bath_url(self):
    url = reverse('bath')
    self.response = self.client.get(url)
    self.assertEqual(self.response.status_code, 200)

  def test_bed_url(self):
    url = reverse('bed')
    self.response = self.client.get(url)
    self.assertEqual(self.response.status_code, 200)

  def test_guest_url(self):
    url = reverse('guest')
    self.response = self.client.get(url)
    self.assertEqual(self.response.status_code, 200)

  def test_office_url(self):
    url = reverse('office')
    self.response = self.client.get(url)
    self.assertEqual(self.response.status_code, 200)
