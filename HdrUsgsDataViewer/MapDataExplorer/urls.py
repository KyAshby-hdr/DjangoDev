from django.urls import path
from . import views

urlpatterns = [
    path('', views.mapExplorer, name='mapExplorer'),
    path('about/', views.about, name='about')
]