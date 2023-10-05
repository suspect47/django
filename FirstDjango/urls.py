from django.urls import path
from MainApp import views

urlpatterns = [
    path("", views.home),
    #path("about", views.about),
    #path("item/<int:number>", views.item),
    #path("items", views.numeric_list),
    path("item/<int:number>", views.item1),
    path("items", views.numeric_list),
    path("index.html", views.index)
]
