# serializers.py
from rest_framework import serializers

from .models import Recipe, RecipeStep, Tag, Categories


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
        fields = ('title', 'description', 'cooking_time_min',
                  'creation_date', 'is_published', 'image',
                  'categories', 'tags')

    categories = CategoriesSerializer(many=True, read_only=True)
    tags = TagSerializer(many=True, read_only=True)
