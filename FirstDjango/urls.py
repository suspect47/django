from django.urls import path
from MainApp import views

urlpatterns = [
    path("item/<int:number>", views.item1),
    path("items", views.items)
]
