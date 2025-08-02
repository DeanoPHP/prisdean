from allauth.account.adapter import DefaultAccountAdapter
from accounts.models import CustomUser


class CustomAccountAdapter(DefaultAccountAdapter):
    def get_phone(self, user):
        # Return user's phone if stored on CustomUser model
        return user.phone

    def get_user_by_phone(self, phone, *args, **kwargs):
        # Allow lookup by phone (or return None if not using phone login)
        try:
            return CustomUser.objects.get(phone=phone)
        except CustomUser.DoesNotExist:
            return None