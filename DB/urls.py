from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="/"),
    path('add-diner/',views.addDiner, name='add-diner'),
]