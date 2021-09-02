from django.urls import path
from . import views  

urlpatterns = [
    path('meetups', views.index, name='all-meetups'),
    #path('meetups_01', views.index_part_01)
    path('meetups/<slug:meetup_slug>', views.meetup_details, name='meetups-details'),  # our-domain.com/meetups/<dynamic-path-segment>
]