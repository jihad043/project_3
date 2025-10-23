from django.urls import path
from .views import *
urlpatterns = [
    
    path("home",home, name="get_data_by_id" ),
    path("list",list, name="list" ),
]
