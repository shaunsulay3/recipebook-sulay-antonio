from django.urls import path
from .views import recipes_list_url, recipe_1_url, recipe_2_url
urlpatterns = [
    path('recipes/list/', recipes_list_url, name='recipes_list_url'),
    path('recipe/1', recipe_1_url, name='recipe_1_url'),
    path('recipe/2', recipe_2_url, name='recipe_2_url'),
]
# This might be needed, depending on your Django version
app_name = "ledger"