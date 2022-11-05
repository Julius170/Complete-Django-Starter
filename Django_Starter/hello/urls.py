from django.urls import path
from . import views 

urlpatterns = [
    path("", views.index, name="index"),
    path("phenzic", views.phenzic, name="phenzic"),
    path("<str:name>", views.greet, name="greet")
]