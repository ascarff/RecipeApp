from django.contrib import admin
from .models import Recipe, Protein, Category

@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    list_display = ["name", "protein"]

@admin.register(Protein)
class ProteinAdmin(admin.ModelAdmin):
    list_display = ["name"]

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ["name"]