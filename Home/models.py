from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Vegetable(models.Model):
    # asdf
    # id = models.AutoField(primary_key=True) it take by default but we can also write it explicitly
    # This creates a relationship between my Recipe model and Django's built-in User model.
    # Each recipe is connected to one user, and one user can have multiple recipes. 
    # If that user is deleted, all recipes created by that user will also be deleted because of CASCADE
    user = models.ForeignKey(User, on_delete=models.CASCADE) # IMPORTANT : Read it's above function
    recipe_name = models.CharField(max_length=100)
    recipe_price = models.DecimalField(max_digits=10, decimal_places=2)
    recipe_description = models.TextField()
    recipe_image = models.ImageField(upload_to='recipe_images/')
