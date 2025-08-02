from django.shortcuts import render
from django.http import HttpResponse



def home(request):
    return HttpResponse("Cleaning Project Homepage — coming soon!")


def about(request):
    return HttpResponse("This is the about page")


def contact(request):
    return HttpResponse("This is the Contact Us page")