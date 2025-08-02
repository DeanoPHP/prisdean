from django.http import HttpResponse


def home(request):
    return HttpResponse("Cleaning Project Homepage — coming soon!")