from django.test import SimpleTestCase,TestCase
from django.urls import reverse,resolve
from .views import Homepage


class Home_page_test (TestCase):

    def setUp(self) -> None:
        url=reverse('Home:main')
        self.response=self.client.get(url)

    def Template_test(self):
        self.assertEqual(self.response.status_code, 200)
        self.assertTemplateUsed(self.response, 'account/register.html')
        self.assertContains(self.response, 'hi')
        self.assertNotContains(self.response, 'not text')

    def View_Test(self):
        view=resolve('account/Register')
        self.assertEqual(view.func.__name__,Homepage.__name__)

# Create your tests here.
