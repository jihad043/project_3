from django.urls import path
from .views import *


urlpatterns = [
    

    path('singup',singup,name="singup")
]
