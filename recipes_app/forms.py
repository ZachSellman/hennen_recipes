from django import forms
from .models import Recipe

# ignore for now, saving for reference; to be removed/updated later
# class RecipesForm(forms.Modelform):
#     class Meta:
#         model = Recipe
#         fields = [
#             "name",
#             "image",
#             "description",
#             "servings",
#             "status",
#             "base_yield",
#             "created_at",
#             "updated_at",
#         ]


class IngredientCreationForm(forms.Form):
    name = forms.CharField()
    image = forms.ImageField()
