from django import forms

class RecipeImageForm(forms.Form):
    image = forms.ImageField(label="Upload Image")
    description = forms.CharField(label = "Description", max_length=255)

class RecipeForm(forms.Form):
    name = forms.CharField(label="Name", max_length=50)
