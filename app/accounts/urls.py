from django.urls import path
from . import views


urlpatterns = [
    path('login/', views.CustomLoginView.as_view(), name='account_login'),
    path('signup/', views.CustomSignupView.as_view(), name='account_signup'),
]