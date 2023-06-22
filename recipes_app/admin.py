from django.contrib import admin
from .models import (
    Recipe,
    Ingredient,
    Measurement,
    Tag,
    RecipeIngredient,
    RecipeStep,
    RecipeNote,
    RecipeTag,
    RecipeReference,
    IngredientVendor,
)

# Register your models here.
admin.site.register(Recipe)
admin.site.register(Ingredient)
admin.site.register(Measurement)
admin.site.register(Tag)
