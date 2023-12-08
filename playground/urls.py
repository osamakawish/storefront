from django.urls import path
from . import views

# Must be named urlpatterns
urlpatterns = [
  path('hello/', views.say_hello)
]