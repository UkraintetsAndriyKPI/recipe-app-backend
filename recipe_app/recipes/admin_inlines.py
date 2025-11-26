from django.contrib import admin
from .models import RecipeCategories, RecipeTags

class RecipeCategoriesInline(admin.TabularInline):
    model = RecipeCategories
    extra = 1
    autocomplete_fields = ['category_id']

class RecipeTagsInline(admin.TabularInline):
    model = RecipeTags
    extra = 1
    autocomplete_fields = ['tag_id']
