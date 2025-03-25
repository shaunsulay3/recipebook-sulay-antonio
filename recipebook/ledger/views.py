from django.shortcuts import render
from .models import Recipe, Ingredient, RecipeImage
from .forms import RecipeImageForm
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

    ctx = {
        'recipe': recipe,
        'ingredients': ingredients
    }
    
    return render(request, "recipe.html",ctx)

def add_image(request,id):
    form = RecipeImageForm()

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
            
    ctx = { 'form': form }
    return render(request, "add_image.html", ctx)
