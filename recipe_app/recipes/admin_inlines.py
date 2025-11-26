from django.contrib import admin
from .models import RecipeCategories, RecipeStep, RecipeTags


class RecipeCategoriesInline(admin.TabularInline):
    model = RecipeCategories
    extra = 1
    autocomplete_fields = ['category_id']

class RecipeTagsInline(admin.TabularInline):
    model = RecipeTags
    extra = 1
    autocomplete_fields = ['tag_id']

class RecipeStepInline(admin.TabularInline):
    model = RecipeStep
    extra = 1
    fields = ('step_number', 'instruction')
    ordering = ('step_number',)
    min_num = 0
    max_num = 10
