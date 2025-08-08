from django.shortcuts import render
from django.views.generic import (
    TemplateView, 
    UpdateView, 
    DeleteView,
)
from django.contrib.auth.mixins import LoginRequiredMixin
from accounts.forms import CustomSignupForm
from django.urls import reverse_lazy


class ProfileView(LoginRequiredMixin, TemplateView):
    template_name = 'userprofile/profile.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)        
        
        user = self.request.user        
        context['profile'] = user.profile
        
        return context
    
    
class UpdateProfile(LoginRequiredMixin, UpdateView):
    template_name = 'userProfile/update_profile.html'
    success_url = reverse_lazy('profile')
    
    
    
class DeleteProfile(LoginRequiredMixin, DeleteView):
    """
    Need to create a signal that deletes the user if
    profile is deleted although I think the model 
    already handles this.
    """ 
    pass
    



