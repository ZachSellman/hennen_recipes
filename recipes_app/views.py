from django.shortcuts import render
from .forms import IngredientCreationForm

# Create your views here.


def index(request):
    return render(request, "recipes_app/index.html")


def create_ingredient(request):
    context = {"form": IngredientCreationForm()}
    return render(request, "recipes_app/ingredient_form.html", context=context)
