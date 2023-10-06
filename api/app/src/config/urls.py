from django.urls import path, include
from src.app.controller import TestController, EventController

urlpatterns = [
    path('test/', TestController.as_view({'get': 'get_result'})),
    path('api/v1/event', EventController.as_view(), name='event')
]
