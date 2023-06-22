# Generated by Django 4.2.2 on 2023-06-21 22:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recipes_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Ingredients',
            new_name='Ingredient',
        ),
        migrations.RenameModel(
            old_name='IngredientVendors',
            new_name='IngredientVendor',
        ),
        migrations.RenameModel(
            old_name='Measurements',
            new_name='Measurement',
        ),
        migrations.RenameModel(
            old_name='Recipes',
            new_name='Recipe',
        ),
        migrations.RenameModel(
            old_name='RecipeIngredients',
            new_name='RecipeIngredient',
        ),
        migrations.RenameModel(
            old_name='RecipeNotes',
            new_name='RecipeNote',
        ),
        migrations.RenameModel(
            old_name='RecipeSteps',
            new_name='RecipeStep',
        ),
        migrations.RenameModel(
            old_name='RecipeTags',
            new_name='RecipeTag',
        ),
        migrations.RenameModel(
            old_name='Tags',
            new_name='Tag',
        ),
    ]
