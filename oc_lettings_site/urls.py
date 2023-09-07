"""
Configuration des URL principales du projet, incluant les applications
"lettings" et "profiles".
"""
from django.contrib import admin
from django.urls import path, include

import oc_lettings_site.views

urlpatterns = [
    path('', oc_lettings_site.views.index, name='index'),
    path('lettings/', include('lettings.urls', namespace='lettings')),
    path('profiles/', include('profiles.urls', namespace='profiles')),
    path('admin/', admin.site.urls),
    # Test de la page 404
    path('404/', oc_lettings_site.views.error_404_view_handler),
]

handler404 = 'oc_lettings_site.views.error_404_view_handler'
handler500 = 'oc_lettings_site.views.error_500_view_handler'
handler403 = 'oc_lettings_site.views.error_403_view_handler'
handler400 = 'oc_lettings_site.views.error_400_view_handler'
