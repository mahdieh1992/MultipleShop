from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse,resolve
from .views import RgisterUser
from .forms import RegisterUserForm


class CreateCustomUser(TestCase):

    def test_create_user(self):
        User = get_user_model()
        user = User.objects.create_user(email='mjdR70@gmail.com',password='123456')
        self.assertEqual(user.email,'mjdR70@gmail.com')
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)
        try:
            self.assertIsNone(user.username)
        except AttributeError:
                pass
        with self.assertRaises(TypeError):
            User.objects.create_user(email='12')

    def test_create_superuser(self):
        User = get_user_model()
        useradmin = User.objects.create_superuser(email='mjdR70@gmail.com', password='123456')
        self.assertEqual(useradmin.email, 'mjdR70@gmail.com')
        self.assertTrue(useradmin.is_active)
        self.assertTrue(useradmin.is_staff)
        self.assertTrue(useradmin.is_superuser)
        try:
            self.assertIsNone(useradmin.username)
        except AttributeError:
            pass
        with self.assertRaises(ValueError):
            User.objects.create_user(email='',password='',is_superuser=False)
# Create your tests here.


class TestRegisterUser(TestCase):
    def setUp(self) -> None:
        url=reverse('account:Register')
        self.response=self.client.get(url)

    def Template_Test(self):
        self.assertEqual(self.response.status_code,200)
        self.assertTemplateUsed(self.response,'account/register.html')
        self.assertContains(self.response,'hi')
        self.assertNotContains(self.response,'not text')

    def Form_Test(self):
        form=self.response.context.get('form')
        self.assertIsInstance(form,RegisterUserForm)
        self.assertContains(self.response,'csrfmiddlewaretoke')

    def View_Test(self):
        view=resolve('account/Register')
        self.assertEqual(view.func.__name__,RgisterUser.__name__)
