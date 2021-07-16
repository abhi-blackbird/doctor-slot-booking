
from django.urls import path,include
from .views import *
from .import views

urlpatterns = [

    path('app', views.app, name='app'),
    path('post_app', views.post_app, name='post_app'),
    path('timeslot', views.timeslot, name='timeslot'),
    
    path('appointment/', views.appointment, name='appointment'),
    #   path('appointment/', views.appointment_handlers, name='appointment'),
    path('thanku/', views.thanku, name='thanku'),
]