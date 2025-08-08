from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import (
    TemplateView,
    DeleteView,
)
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .forms import CombinedUserProfileForm
from accounts.models import CustomUser


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
    model = CustomUser()
    success_url = reverse_lazy('home')
    template_name = 'userprofile/confirm_delete.html'
    
    def get_object(self):
        return self.request.user
    
    



