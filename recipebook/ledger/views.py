from django.shortcuts import render
from django.http import HttpResponse
from .models import Recipe, Ingredient, RecipeIngredient
# Create your views here.



def recipes_list_url(request):

    recipes = Recipe.objects.all()
    ctx = { "recipes": recipes }
    return render(request, "recipes_list.html", ctx)


def recipe(request,id):

    recipe = Recipe.objects.get(id=id)
    ingredients = Ingredient.objects.filter(recipe__recipe__name=recipe.name)
    print(ingredients)

    ctx = {
        'recipe': recipe,
        'ingredients': ingredients
    }
    
    return render(request, "recipe.html",ctx)
