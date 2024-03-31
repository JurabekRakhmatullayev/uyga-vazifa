from django.urls import path
from . import views
urlpatterns = [
    # path("",views.main,name="home/"),
    # path("hello/<str:name>/", "),
    path("hello/",views.main,name="hello"),
    # path("",views.main,name="help/"),
]