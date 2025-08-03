from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required
def userProfilePage(request):
    profile = request.profile.user
    
    return render(request, 'profile.html', {'profile': profile})


