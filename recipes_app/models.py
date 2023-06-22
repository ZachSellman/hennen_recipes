from django.db import models

# Create your models here.


class Recipe(models.Model):
    """Model for a Recipe"""

    name = models.CharField(max_length=120, unique=True, null=False)
    image = models.ImageField(default="default.jpg", upload_to="recipe-images")
    description = models.CharField(max_length=4000)
    servings = models.IntegerField()
    status = models.CharField(max_length=10, default="private", null=False)
    base_yield = models.CharField(max_length=120)
    created_at = models.DateTimeField(auto_now_add=True, null=False)
    updated_at = models.DateTimeField(auto_now=True, null=False)

    def __str__(self):
        return f"{self.name} Recipe"


class Ingredient(models.Model):
    """Model for an individual ingredient"""

    name = models.CharField(max_length=120, unique=True, null=False)
    image = models.ImageField(default="default.jpg", upload_to="ingredient-images")
    updated_at = models.DateTimeField(auto_now=True, null=False)


class Measurement(models.Model):
    """Model for all Measurements"""

    name = models.CharField(max_length=50, unique=True, null=False)
    base_maxiumum = models.IntegerField()
    unit_up = models.ForeignKey(
        "self",
        default=None,
        related_name="%(class)s_unit_size_up",
        on_delete=models.SET_DEFAULT,
    )
    unit_down = models.ForeignKey(
        "self",
        related_name="%(class)s_unit_size_down",
        default=None,
        on_delete=models.SET_DEFAULT,
    )


class Tag(models.Model):
    """Model for a list of possible tags for Recipes"""

    tag_name = models.CharField(
        max_length=25, unique=True, primary_key=True, null=False
    )


class RecipeIngredient(models.Model):
    """Model for an ingredient that exists in a Recipe"""

    recipe_id = models.ForeignKey(Recipe, on_delete=models.CASCADE, null=False)
    ingredient_id = models.ForeignKey(Ingredient, on_delete=models.PROTECT, null=False)
    measurement_type = models.ForeignKey(
        Measurement, on_delete=models.PROTECT, null=False
    )
    measurement_quantity = models.DecimalField(
        decimal_places=2, max_digits=10, null=False
    )


class RecipeStep(models.Model):
    """Model for the steps of a Recipe"""

    recipe_id = models.ForeignKey(Recipe, on_delete=models.CASCADE, null=False)
    number = models.IntegerField()
    description = models.CharField(max_length=500, null=False)
    updated_at = models.DateTimeField(auto_now=True, null=False)


class RecipeNote(models.Model):
    """Model for the notes of a Recipe"""

    recipe_id = models.ForeignKey(Recipe, on_delete=models.CASCADE, null=False)
    description = models.CharField(max_length=2000, null=False)
    updated_at = models.DateTimeField(auto_now=True, null=False)


class RecipeTag(models.Model):
    """Model for tags of given Recipe"""

    recipe_id = models.ForeignKey(Recipe, on_delete=models.CASCADE, null=False)
    tag_id = models.ForeignKey(Tag, on_delete=models.CASCADE, null=False)


class RecipeReference(models.Model):
    """Model for reference of this recipe to another (new)"""

    recipe_id = models.ForeignKey(
        Recipe, related_name="old_recipe", on_delete=models.CASCADE, null=False
    )
    new_recipe = models.ForeignKey(
        Recipe, related_name="new_recipe", on_delete=models.CASCADE, null=False
    )
    description = models.CharField(max_length=500, null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=False)


class IngredientVendor(models.Model):
    """Model for vendors where an ingredient was purchased from"""

    ingredient_id = models.ForeignKey(Ingredient, on_delete=models.CASCADE, null=False)
    vendor_name = models.CharField(max_length=120, unique=True, null=False)
    image = models.ImageField(default="default.jpg", upload_to="vendor-images")
    description = models.CharField(max_length=2000)
    created_at = models.DateTimeField(auto_now_add=True, null=False)
    updated_at = models.DateTimeField(auto_now=True, null=False)
