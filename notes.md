# Build containers
docker-compose build

# Run containers
docker-compose up

# Django commands
- docker-compose run web python app/manage.py makemigrations
- docker-compose run web python app/manage.py migrate
- docker-compose run web python app/manage.py createsuperuser

# PostgreSQL Docker + `psql` Command Cheat Sheet

## Access psql

```sql
docker exec -it prisdean-db-1 psql -U deanlark prisdean
```

## List Databases

```sql
\l
```

---

## Connect to a Database

```sql
\c prisdean
```

---

## List All Tables

```sql
\dt
```

List tables across all schemas:

```sql
\dt *.*
```

---

## Describe a Table (Structure)

```sql
\d table_name
```

Example:

```sql
\d accounts_customuser
```

---

## Show Columns in a Table

```sql
SELECT column_name
FROM information_schema.columns
WHERE table_name = 'accounts_customuser';
```

---

## Select All Data from a Table

```sql
SELECT * FROM table_name;
```

Example:

```sql
SELECT * FROM accounts_customuser;
```

---

## Limit Number of Rows

```sql
SELECT * FROM table_name LIMIT 10;
```

---

## 10. Exit `psql`

```sql
\q
```

---

## One-Liner Query from Outside Container

If you don’t want to enter bash, you can run:

```bash
docker exec -it <container_name> psql -U <username> -d <database_name> -c "SELECT * FROM accounts_customuser;"
```

Example:

```bash
docker exec -it postgres-container psql -U deanlark -d prisdean -c "SELECT * FROM accounts_customuser;"
```

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

# Testing template
```python
from django.test import SimpleTestCase
from django.urls import reverse

class HomePageTests(SimpleTestCase):
    def url_exists_at_correct_location(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_homepage_url_name(self):
        response = self.client.get('home')
        self.assertEqual(response.status_code, 200)
```