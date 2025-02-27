from django.urls import path
from .views import recipes_list_url, recipe
urlpatterns = [
    path('recipes/list/', recipes_list_url, name='recipes_list_url'),
    path('recipe/<int:id>', recipe, name='recipe'),
]
# This might be needed, depending on your Django version
app_name = "ledger"