from django.shortcuts import render
from .models import Recipe, Ingredient
# Create your views here.



def recipes_list(request):

    recipes = Recipe.objects.all()
    ctx = { "recipes": recipes }
    return render(request, "recipes_list.html", ctx)


def recipe(request,id):

    recipe = Recipe.objects.get(id=id)
    ingredients = Ingredient.objects.filter(recipe__recipe__name=recipe.name)

    ctx = {
        'recipe': recipe,
        'ingredients': ingredients
    }
    
    return render(request, "recipe.html",ctx)
