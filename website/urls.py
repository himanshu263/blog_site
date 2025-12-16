from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('service/', views.service, name='service'),
    path('project/', views.project, name='project'),
    path('team/', views.team, name='team'),
    path('testimonial/', views.testimonial, name='testimonial'),
     path('contact/', views.contact, name='contact')
]