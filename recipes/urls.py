from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("get-all-active-recipes", views.get_all_active_recipes, name="get_all_active_recipes")
]