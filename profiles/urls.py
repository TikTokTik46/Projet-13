"""
Configuration des URL pour l'application "profiles".
"""
from django.urls import path
import profiles.views

app_name = 'profiles'

urlpatterns = [
    path('', profiles.views.index, name='profiles_index'),
    path('<str:username>/', profiles.views.profile, name='profile'),
]
