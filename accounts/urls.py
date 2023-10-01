from django.urls import path
from .views import *

urlpatterns = [
    path('auth-user/', auth_user, name='auth-user')
]