from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("ingredient_form", views.create_ingredient, name="create_ingredient"),
]
