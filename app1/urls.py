from django.urls import path
from .views import home_view,submit_contact

urlpatterns = [
    path('',home_view,name='home_view'),
    path('contact/',submit_contact,name='contact'),
]