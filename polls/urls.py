from django.urls import path

from . import views

urlpatterns = [
    path("", views.chart, name="chart"),
    path("home", views.home),
    #path("chart", views.chart),    
]
