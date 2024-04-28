from django.urls import path
from .views import say_hello


urlpatterns = [
    path("/<str:name>", say_hello),
]
