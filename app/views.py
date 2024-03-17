from django.shortcuts import *
from .models import Recipe
# Create your views here.
# def home(request):
#     if request.method=="POST":
#         recipeName=request.POST.get('recipeName')
#         recipeDescription=request.POST.get('recipeDescription')
#         recipeImage=request.POST.get('recipeImage')
#         recipe=Recipe.objects.create(recipeName=recipeName,recipeDescription=recipeDescription,recipeImage=recipeImage)
#         recipe.save()
#     return render(request,'home.html')

from django import forms
from .models import Recipe


class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ['recipeName', 'recipeDescription', 'recipeImage']


def home(request):
    if request.method == "POST":
        form = RecipeForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = RecipeForm()
    return render(request, 'home.html', {'form': form})

#TO Retiireve Data from databse to front_end
def recipe_list(request):
    recipes = Recipe.objects.all()
    return render(request, 'recipelist.html', {'recipes': recipes})


#view Funtion
def source(request,id):
    recipe=Recipe.objects.get(id=id)
    return render(request,'source.html',{'know':recipe})



#search function
def search(request):
    query=request.GET.get('query')
    if query:
        recipes=Recipe.objects.filter(recipeName__icontains=query)
    else:
        recipes=Recipe.objects.all()
    return render(request, 'recipelist.html', {'recipes': recipes})


