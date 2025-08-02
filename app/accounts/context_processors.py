from allauth.account.forms import LoginForm
from accounts.forms import CustomSignupForm

def auth_forms(request):
    return {
        'login_form': LoginForm(),
        'signup_form': CustomSignupForm(),
    }
