from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('rooms/', views.rooms, name='rooms'),
    path('report/', views.report, name='report'),
    path('reservation/', views.reservation, name='reservation'),
    path('reservation-add/', views.addReservation, name='addReservation'),
    path('availability/', views.check_av, name='check_av'),
    path('', include('django.contrib.auth.urls')),
]