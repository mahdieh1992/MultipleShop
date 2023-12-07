from django.test import SimpleTestCase
from django.urls import reverse,resolve
from .views import Homepage


class Home_page_test (SimpleTestCase):
    def setUp(self) -> None:
        url=reverse('Home:main')
        self.response= self.client.get(url)

    def url_exists(self):
        self.assertEqual(self.response.status_code,200)

    def templated_exits(self):
        self.assertTemplateUsed(self.response)

    def contain_htmltext(self):
        self.assertContains(self.response,'hi')

    def not_contain_htmltext(self):
        self.assertNotContains(self.response, 'I should not page')

    def test_url_resolve_View(self):
        view=resolve('/')
        self.assertEqual(view.func.__name__,Homepage.as_view().__name__)
# Create your tests here.
