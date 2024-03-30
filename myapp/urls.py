from django.urls import path
from . import views
urlpatterns = [
    path("",views.main,name="home/"),
    path("",views.main,name="hello/"),
    path("",views.main,name="help/"),
]