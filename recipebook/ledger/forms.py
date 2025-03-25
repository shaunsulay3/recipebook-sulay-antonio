from django import forms

class RecipeImageForm(forms.Form):
    image = forms.ImageField(label="Upload Image")
    description = forms.CharField(label = "Description: ", max_length=255)