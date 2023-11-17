from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Food_Taken(models.Model):
    Name = models.CharField(max_length=200,blank=True)
    Protein = models.FloatField()
    Fats = models.FloatField()
    Carbohydrates = models.FloatField()
    Calories = models.FloatField()

    def __str__(self):
        return self.Name

class Consumer_Info(models.Model):
    User_Detail = models.ForeignKey(User,on_delete=models.CASCADE)
    Food_Consumed = models.ForeignKey(Food_Taken,on_delete=models.CASCADE)