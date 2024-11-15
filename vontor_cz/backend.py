from django.contrib.auth.backends import BaseBackend
from django.contrib.auth import get_user_model


class EmailOrUsernameModelBackend(BaseBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        print('custom backend used')

        UserModel = get_user_model()
        if '@' in username:
            # If "@" is present, treat it as an email address
            try:
                user = UserModel.objects.get(email=username)
            except UserModel.DoesNotExist:
                return None
        else:
            # Otherwise, treat it as a username
            user = UserModel.objects.filter(username=username).first()

        if user and user.check_password(password):
            return user
        return None

    def get_user(self, user_id):
        UserModel = get_user_model()
        try:
            return UserModel.objects.get(pk=user_id)
        except UserModel.DoesNotExist:
            return None