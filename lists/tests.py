from django.test import TestCase

# Create your tests here.
class SmokeTest(TestCase):

    def testy(self):
        self.assertEqual(1, 2)
