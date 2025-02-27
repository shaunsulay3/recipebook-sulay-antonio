from django.db import models
from django.urls import reverse

# Create your models here.
class Recipe(models.Model):
    name = models.CharField(max_length=50)
    def get_absolute_url(self):
        return( reverse('ledger:recipe', args=[str(self.id)]))
    def __str__(self):
        return self.name
    
class Ingredient(models.Model):
    name = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name
    

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
    def __str__(self):
        return (self.recipe.name + ": " + self.quantity + " " + self.ingredient.name) 
    

