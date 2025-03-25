from django.shortcuts import render, redirect
from .models import Recipe, Ingredient, RecipeImage, Profile
from .forms import RecipeImageForm, RecipeForm
from django.contrib.auth.decorators import login_required
# Create your views here.



def recipes_list(request):

    recipes = Recipe.objects.all()
    ctx = { "recipes": recipes }
    return render(request, "recipes_list.html", ctx)

@login_required
def recipe(request,id):

    recipe = Recipe.objects.get(id=id)
    ingredients = Ingredient.objects.filter(recipe__recipe__name=recipe.name)
    recipe_image = recipe.image.all()
    if recipe_image:
        recipe_image = recipe_image[0]
    else:
        recipe_image = None

    ctx = {
        'recipe': recipe,
        'ingredients': ingredients,
        'recipe_image': recipe_image
    }
    
    return render(request, "recipe.html",ctx)

def add_image(request,id):
    form = RecipeImageForm()
    recipe = Recipe.objects.get(id=id)

    if request.method == 'POST':
        print('helloadsfns')

        # Creating a Form object
        form = RecipeImageForm(request.POST, request.FILES)
        # Checking if the inputs are valid
        if form.is_valid():
            print('valid')

            ri = RecipeImage()
            ri.image = form.cleaned_data.get('image')
            ri.description = form.cleaned_data.get('description')
            ri.recipe = Recipe.objects.get(id=id)
            ri.save()
            
    ctx = { 
        'form': form,
        'recipe': recipe
    }
    return render(request, "add_image.html", ctx)

def add_recipe(request):
    form = RecipeForm()

    if request.method == 'POST':

        form = RecipeForm(request.POST)

        if form.is_valid():
            r = Recipe()
            r.name = form.cleaned_data.get('name')
            r.author = Profile.objects.get(user=request.user)
            r.save()

            ctx= {'recipe': r}
            print(ctx)
            return render(request, "add_image.html", ctx)
    
    ctx = { 'form': form }
    return render(request, "add_recipe.html", ctx)

