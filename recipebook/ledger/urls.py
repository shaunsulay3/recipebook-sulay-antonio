from django.urls import path
from .views import recipes_list, recipe
urlpatterns = [
    path('recipes/list/', recipes_list, name='recipes_list'),
    path('recipe/<int:id>', recipe, name='recipe'),
]
# This might be needed, depending on your Django version
app_name = "ledger"