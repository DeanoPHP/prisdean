from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import (
    TemplateView, 
    UpdateView, 
    DeleteView,
)
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .forms import CombinedUserProfileForm


class ProfileView(LoginRequiredMixin, TemplateView):
    template_name = 'userprofile/profile.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)        
        
        user = self.request.user        
        context['profile'] = user.profile
        
        return context
    
    
class UpdateProfileView(LoginRequiredMixin, View):
    def get(self, request):
        form = CombinedUserProfileForm(
            user_instance=request.user,
            profile_instance=request.user.profile
        )
        
        return render(request, 'userprofile/update_profile.html', {'form': form})
    
    def post(self, request):
        form = CombinedUserProfileForm(
            request.POST, request.FILES,
            user_instance=request.user,
            profile_instance=request.user.profile
        )
        if form.is_valid():
            form.save()
            return redirect('profile')
        return render(request, 'userprofile/update_profile.html', {'form': form})
    
    
    
class DeleteProfileView(LoginRequiredMixin, DeleteView):
    """
    Need to create a signal that deletes the user if
    profile is deleted although I think the model 
    already handles this.
    """ 
    pass
    



