from django.urls import path
from . import views
from django.conf.urls import url

urlpatterns = [
    path('sightings/', views.index),
    path('sightings/new/', views.create_view, name='add'),
    path('map/', views.showmap, name='showmap'),
    path('sightings/stats/', views.stats, name='stats'),
    path('sightings/<squirrel_id>/', views.update, name='update'),
    path('sightings/<squirrel_id>/delete/', views.delete, name='delete'),
]
