from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin


class ProfileView(LoginRequiredMixin, TemplateView):
    template_name = 'userprofile/profile.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)        
        
        user = self.request.user        
        context['profile'] = user.profile
        
        return context
    



