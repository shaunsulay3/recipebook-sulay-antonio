from django.db import models

# Create your models here.
class Recipe(models.Model):
    name = models.CharField(max_length=50)
    #ingredients = recipeingredient.ingrendient


class Ingredient(models.Model):
    name = models.CharField(max_length=50)
    #recipe = recipeingredient.recipe

class RecipeIngredient(models.Model):
    quantity = models.CharField(max_length=10)
    ingredient = models.ForeignKey(
        Ingredient, 
        on_delete=models.CASCADE,
        related_name="recipe"
    )
    recipe = models.ForeignKey(
        Recipe, 
        on_delete=models.CASCADE,
        related_name="ingredients"
    )
    

