from django.contrib import admin
from django.urls import path, include

import oc_lettings_site.views

urlpatterns = [
    path('', oc_lettings_site.views.index, name='index'),
    path('lettings/', include('lettings.urls', namespace='lettings')),
    path('profiles/', include('profiles.urls', namespace='profiles')),
    path('admin/', admin.site.urls),
]
