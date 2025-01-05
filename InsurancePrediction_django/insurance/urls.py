from django.urls import path,include
from . import views

urlpatterns = [
    path("",views.homepage),
    path("home",views.homepage, name="home"),
    path("about",views.about, name="about"),
    path("contact",views.contact, name="contact"),
    path("prediction",views.prediction, name="prediction"),
    path("results",views.results, name="results"),


]