from django.db import models


# Create your models here.
from django.db import models

class Recipe(models.Model):
    recipeName = models.CharField(max_length=100)
    recipeDescription = models.TextField()
    recipeImage = models.ImageField(upload_to='recipe_images/', default='default_image.jpg')
