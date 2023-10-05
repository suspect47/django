from django.urls import path
from MainApp import views

urlpatterns = [
    path("", views.home),
    path("item/<int:number>", views.item1),
    path("items", views.numeric_list),
    path("index.html", views.index)
]
