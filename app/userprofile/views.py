from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def userProfilePage(request):
    profile = request.user.profile

    context = {
        'profile': profile
    }

    return render(request, 'userprofile/profile.html', context)



