from django.contrib import admin

from recipes.admin_inlines import RecipeCategoriesInline, RecipeTagsInline, RecipeStepInline

from .models import DailyRecipe, Tag, Categories, Recipe


@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "description", "cooking_time_min", "creation_date", "is_published", "image")
    search_fields = ("title", "description")
    list_filter = ("categories", "tags")
    ordering = ("-id",)

    inlines = [RecipeCategoriesInline, RecipeTagsInline, RecipeStepInline]

@admin.register(Categories)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "category_name")
    search_fields = ("category_name",)

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ("id", "tag_name")
    search_fields = ("tag_name",)

@admin.register(DailyRecipe)
class DailyRecipeAdmin(admin.ModelAdmin):
    list_display = ("id", "date", "recipe")
    search_fields = ("date",)
    ordering = ("-date",)
