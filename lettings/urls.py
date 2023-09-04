from django.urls import path

import lettings.views

app_name = 'lettings'

urlpatterns = [
    path('', lettings.views.index, name='lettings_index'),
    path('<int:letting_id>/', lettings.views.letting, name='letting'),
]
