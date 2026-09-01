from django.urls import path
from . import views
urlpatterns = [
  path("", views.index, name="index"),
  path("<str:name>", views.greet, name="greet"),
  path("khoa", views.khoa, name="khoa"),
  path("david", views.david, name="David")
]