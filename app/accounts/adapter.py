from allauth.account.adapter import DefaultAccountAdapter


class CustomAccountAdapter(DefaultAccountAdapter):
    def get_phone(self, user):
        # Return user's phone if stored on CustomUser model
        return user.phone
