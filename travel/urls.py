from django.urls import path
from . import views


urlpatterns = [
    path('',views.index,name='index'),
    path('news/',views.news,name='news'),
    path('destinations/',views.destinations,name='destinations'),
    path('contact/',views.contact,name='contact'),
    path('element/',views.element,name='element'),
    path('feedback/',views.feedback,name='feedback'),
]