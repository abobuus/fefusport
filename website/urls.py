from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='home'),
    path('addpage/', addpage, name='add_page'),
]
