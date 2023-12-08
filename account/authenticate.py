from django.contrib.auth.backends import BaseBackend
from .models import CustomUser


class AuthenticateUser(BaseBackend):
    def authenticate(self, request, email=None, password=None):
        try:
            user=CustomUser.objects.get(Mobile=email)

        except CustomUser.DoesNotExist:
            return None
        else:
            if user.check_password(password):
                return user

    def get_user(self, user_id):
        try:
            return CustomUser.objects.get(pk=user_id)
        except CustomUser.DoesNotExist:
            return None
