from django.urls import path
from api import views

urlpatterns = [
    # learning interface test:
    # ex : /v1/hello_world/
    path(r'hello_api/', views.hello_api),
    path(r'get_events/', views.get_events),
    path(r'get_event/', views.get_event),
]