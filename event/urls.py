from django.urls import path
from .views import *

urlpatterns = [
    path('view-events', view_events),
    path('post-event', create_event),
]
