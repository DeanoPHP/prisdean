from django.shortcuts import render
from django.views.generic import TemplateView
from accounts.forms import CustomSignupForm
from allauth.account.forms import LoginForm



class Home(TemplateView):
    template_name = "pages/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['login_form'] = LoginForm()
        context['signup_form'] = CustomSignupForm()
        return context
    

class About(TemplateView):
    template_name = 'pages/about.html'


class Contact(TemplateView):
    template_name = 'pages/contact.html'