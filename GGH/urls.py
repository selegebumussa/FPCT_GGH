from GGH.models import Membership
from django.urls import path
from . import views

urlpatterns = [
    path('', views.base, name ='base'),
    path('about/', views.about, name ='about'),
    
    path('testimonial/', views.testimonial, name ='testimonial'),
    
    path('blog/', views.blog, name ='blog'),
    path('contact', views.contact, name ='contact'),
    path('watoto_vijana/', views.watoto_vijana, name ='watoto_vijana'),
    path('sifa_mziki/', views.sifa_mziki, name ='sifa_mziki'),
    path('tehama/', views.tehama, name='tehama'),
    
    path('wanawake/', views.wanawake, name='wanawake'),

    path('misheni/' , views.misheni, name="misheni"),
    path('tunachoamini/' , views.tunachoamini, name="tunachoamini"),
    path('maadili/' , views.maadili, name="maadili"),
    path('membership/', views.membership, name="membership")




]
