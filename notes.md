# Build containers
docker-compose build

# Run containers
docker-compose up

# Django commands
- docker-compose run web python app/manage.py makemigrations
- docker-compose run web python app/manage.py migrate
- docker-compose run web python app/manage.py createsuperuser

# Access psql
docker exec -it prisdean-db-1 psql -U deanlark prisdean

# Delete a user by email
DELETE FROM accounts_customuser WHERE email='example@email.com';

# Use email for login instead of username
ACCOUNT_LOGIN_METHODS = {'email'}

# Fields required at signup (phone/address handled in CustomSignupForm)
ACCOUNT_SIGNUP_FIELDS = ['email*', 'password1*', 'password2*']

# Disable email verification (can enable later for production)
ACCOUNT_EMAIL_VERIFICATION = 'none'

# Redirects after login/logout
LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/'

# Custom forms and adapter
ACCOUNT_FORMS = {
    'signup': 'accounts.forms.CustomSignupForm',
}
ACCOUNT_ADAPTER = 'accounts.adapter.CustomAccountAdapter'

# Static files
STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / 'static']
STATIC_ROOT = BASE_DIR / 'staticfiles'

# Media files
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

# accounts/forms.py

```python
from allauth.account.forms import SignupForm
from django import forms
from .models import CustomUser

class CustomSignupForm(SignupForm):
    phone = forms.CharField(max_length=20, required=False)
    address_line_1 = forms.CharField(max_length=255, required=False)
    city = forms.CharField(max_length=100, required=False)
    postcode = forms.CharField(max_length=20, required=False)

    def save(self, request):
        user = super(CustomSignupForm, self).save(request)
        user.phone = self.cleaned_data.get('phone')
        user.address_line_1 = self.cleaned_data.get('address_line_1')
        user.city = self.cleaned_data.get('city')
        user.postcode = self.cleaned_data.get('postcode')
        user.save()
        return user

```

# accounts/adapter.py

```python
from allauth.account.adapter import DefaultAccountAdapter

class CustomAccountAdapter(DefaultAccountAdapter):
    def get_phone(self, user):
        """
        Returns the user's phone number for use in phone-based flows.
        Currently not used for login but stored in CustomUser.
        """
        return user.phone

    def get_user_by_phone(self, phone, *args, **kwargs):
        """
        Fallback for phone-based login if implemented later.
        Currently returns None to avoid triggering phone login.
        """
        return None
```