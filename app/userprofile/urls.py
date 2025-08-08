from django.urls import path
from . import views


urlpatterns = [
    path('', views.ProfileView.as_view(), name='profile'),
    path('update/', views.UpdateProfileView.as_view(), name='update'),
    path('delete/', views.DeleteProfileView.as_view(), name='delete'),
]


