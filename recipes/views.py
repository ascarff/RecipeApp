from django.shortcuts import render
from django.http import HttpResponse
from .models import Recipe

def index(request):
    return HttpResponse("Hello! Welcome to the recipes app!")


def get_all_active_recipes(request):
    recipes = Recipe.objects.filter(active=True)
    stringy = ''
    for recipe in recipes:
        stringy = stringy + recipe.name + '\n'
    return HttpResponse(stringy)