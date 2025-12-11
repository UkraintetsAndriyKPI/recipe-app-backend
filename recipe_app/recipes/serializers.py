# serializers.py
from rest_framework import serializers

from .models import Recipe, RecipeStep, Tag, Categories, RecipeIngredient


class RecipeIngredientSerializer(serializers.ModelSerializer):
    ingredient_name = serializers.CharField(source='ingredient.name', read_only=True)
    unit = serializers.CharField(source='ingredient.unit', read_only=True)
    class Meta:
        model = RecipeIngredient
        fields = ('ingredient_name', 'quantity', 'unit', 'position')

class CategoriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categories
        fields = ('__all__')

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'

class RecipeStepSerializer(serializers.ModelSerializer):
    class Meta:
        model = RecipeStep
        fields = ('step_number', 'instruction')

class RecipeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Recipe
        fields = ('id', 'title', 'description', 'cooking_time_min',
                  'creation_date', 'is_published', 'image',
                  'categories', 'tags')

    categories = CategoriesSerializer(many=True, read_only=True)
    tags = TagSerializer(many=True, read_only=True)
