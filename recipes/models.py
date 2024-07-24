from django.db import models

class Protein(models.Model):
    name = models.CharField(max_length=30)
    
    def __str__(self) -> str:
        return " ".join(map(str,[self.name]))

class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self) -> str:
        return " ".join(map(str,[self.name]))


class Recipe(models.Model):
    name = models.CharField(max_length=300)
    prep_time = models.IntegerField(blank=True, null=True)
    cook_time = models.IntegerField(blank=True, null=True)
    protein = models.ForeignKey('Protein', on_delete=models.SET_NULL, blank=True, null=True)
    ingredients = models.TextField(blank=True, null=True)
    instructions = models.TextField(blank=True, null=True)
    macros = models.TextField(blank=True, null=True)
    category = models.ManyToManyField('Category', blank=True)


    def __str__(self) -> str:
        return " ".join(map(str,[self.name]))



