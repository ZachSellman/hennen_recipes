from django.db import models

# Create your models here.


class Recipes(models.Model):
    """Model for a Recipe"""

    name = models.CharField(max_length=120, unique=True, null=False)
    image = models.ImageField(default="default.jpg", upload_to="recipe-images")
    description = models.CharField(max_length=4000)
    servings = models.IntegerField()
    status = models.CharField(max_length=10, default='private', null=False)
    base_yield = models.CharField(max_length=120)
    created_at = models.DateTimeField(auto_now_add=True, null=False)
    updated_at = models.DateTimeField(auto_now=True, null=False)


class Ingredients(models.Model):
    """Model for an individual ingredient"""

    name = models.CharField(max_length=120, unique=True, null=False)
    image = models.ImageField(default="default.jpg", upload_to="ingredient-images")
    latest_vendor = models.ForeignKey(
        "IngredientVendors.vendor_name", default=None, on_delete=models.SET_DEFAULT
    )
    updated_at = models.DateTimeField(auto_now=True, null=False)


class Measurements(models.Model):
    """Model for all Measurements"""

    name = models.CharField(max_length=50, unique=True, null=False)
    base_maxiumum = models.IntegerField(null=True)
    unit_up = models.ForeignKey("self", on_delete=models.SET_DEFAULT, null=True)
    unit_down = models.ForeignKey("self", on_delete=models.SET_DEFAULT, null=True)


class Tags(models.Model):
    """Model for a list of possible tags for Recipes"""

    tag_name = models.CharField(max_length=25, unique=True, primary_key=True, null=False)


class RecipeIngredients(models.Model):
    """Model for an ingredient that exists in a Recipe"""

    recipe_id = models.ForeignKey(Recipes.id, on_delete=models.CASCADE, null=False)
    ingredient_id = models.ForeignKey(Ingredients.id, on_delete=models.PROTECT, null=False)
    measurement_type = models.ForeignKey(Measurements.id, on_delete=models.PROTECT, null=False)
    measurement_quantity = models.DecimalField(decimal_places=2, null=False)


class RecipeSteps(models.Model):
    """Model for the steps of a Recipe"""

    recipe_id = models.ForeignKey(Recipes.id, on_delete=models.CASCADE, null=False)
    number = models.IntegerField(null=False)
    description = models.CharField(max_length=500, null=False)
    updated_at = models.DateTimeField(auto_now=True, null=False)


class RecipeNotes(models.Model):
    """Model for the notes of a Recipe"""

    recipe_id = models.ForeignKey(Recipes.id, on_delete=models.CASCADE, null=False)
    description = models.CharField(max_length=2000, null=False)
    updated_at = models.DateTimeField(auto_now=True, null=False)


class RecipeTags(models.Model):
    """Model for tags of given Recipe"""

    recipe_id = models.ForeignKey(Recipes.id, on_delete=models.CASCADE, null=False)
    tag_id = models.ForeignKey(Tags.tag_name, on_delete=models.CASCADE, null=False)


class RecipeReference(models.Model):
    """Model for reference of this recipe to another (new)"""

    recipe_id = models.ForeignKey(Recipes.id, null=False, on_delete=models.CASCADE, null=False)
    new_recipe = models.ForeignKey(Recipes.id, null=False on_delete=models.CASCADE, null=False)
    description = models.CharField(max_length=500, null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=False)


class IngredientVendors(models.Model):
    """Model for vendors where an ingredient was purchased from"""

    ingredient_id = models.ForeignKey(Ingredients.id, null=False, on_delete=models.CASCADE, null=False)
    vendor_name = models.CharField(max_length=120, unique=True, null=False)
    image = models.ImageField(default="default.jpg", upload_to="vendor-images")
    description = models.CharField(max_length=2000)
    created_at = models.DateTimeField(auto_now_add=True, null=False)
    updated_at = models.DateTimeField(auto_now=True, null=False)
