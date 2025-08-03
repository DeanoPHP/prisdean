from django.urls import path
from . import views


urlpatterns = [
    path('', views.userProfilePage, name='profilepage')
]


