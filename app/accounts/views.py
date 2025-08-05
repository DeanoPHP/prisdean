from allauth.account.views import SignupView, LoginView
from django.shortcuts import render


class CustomLoginView(LoginView):
    template_name = 'pages/index.html'
    success_url = '/profile/'

    def form_invalid(self, form):
        """
        On login error, re-render index.html with errors
        and auto-open the login modal.
        """
        return render(self.request, "pages/index.html", {
            "login_form": form,  
            "show_login_modal": True,  
        })
    

class CustomSignupView(SignupView):
    template_name = 'pages/index.html'
    success_url = '/profile/'

    def form_invalid(self, form):
        """
        On signup error, re-render index.html with errors
        and auto-open the signup modal.
        """
        return render(self.request, "pages/index.html", {
            "signup_form": form,
            "show_register_modal": True,
        })