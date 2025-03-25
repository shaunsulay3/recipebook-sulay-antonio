from django.urls import path
from .views import recipes_list, recipe, add_image
urlpatterns = [
    path('recipes/list/', recipes_list, name='recipes_list'),
    path('recipe/<int:id>', recipe, name='recipe'),
    path('recipe/<int:id>/add_image', add_image, name='add_image'),
]
# This might be needed, depending on your Django version
app_name = "ledger"