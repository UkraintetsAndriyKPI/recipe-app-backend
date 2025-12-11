from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import viewsets, status
from django.db.models import Q

from .models import Categories, DailyRecipe, Recipe, Tag
from .serializers import (
    CategoriesSerializer,
    RecipeIngredientSerializer,
    RecipeSerializer,
    RecipeStepSerializer,
    TagSerializer,
)


class RecipeViewSet(viewsets.ModelViewSet):
    queryset = Recipe.objects.filter(is_published=True)
    serializer_class = RecipeSerializer
    ordering_fields = ['creation_date', 'title']
    ordering = ['-creation_date']

    @action(detail=False, methods=['get'], url_path='all-recipes')
    def all_recipes(self, request):
        """
        Returns all Recipe objects, including unpublished ones (for staff users only)
        """
        if not request.user.is_staff:
            return Response(
                {"detail": "You do not have permission to view unpublished recipes."},
                status=status.HTTP_403_FORBIDDEN
            )

        queryset = Recipe.objects.all()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    @action(detail=False, methods=['get'], url_path='daily-recipes')
    def daily_recipes(self, request):
        """
        Returns last 3 DailyRecipe objects with related recipes
        """
        latest_daily = DailyRecipe.objects.filter(recipe__is_published=True).order_by('-date')[:3]
        recipes = [d.recipe for d in latest_daily]
        serializer = self.get_serializer(recipes, many=True)
        return Response(serializer.data)

    @action(detail=True, methods=['get'], url_path='steps')
    def get_steps(self, request, pk=None):
        """
        Returns the steps for a specific recipe
        """
        recipe = self.get_object()
        steps = recipe.recipestep_set.all().order_by('step_number')
        serializer = RecipeStepSerializer(steps, many=True)
        return Response(serializer.data)

    @action(detail=True, methods=['get'], url_path='ingredients')
    def get_ingredients(self, request, pk=None):
        recipe = self.get_object()
        ingredients = recipe.ingredient_links.all().order_by('position')
        serializer = RecipeIngredientSerializer(ingredients, many=True)
        return Response(serializer.data)

    @action(detail=False, methods=['get'], url_path='filter')
    def filter_recipes(self, request):
        """
        Filter recipes by multiple tags and categories.
        Example: /recipes/filter/?tag=1,3&category=2&min_time=10&max_time=30&search=soup
        """
        queryset = Recipe.objects.filter(is_published=True)

        # Tag and Category filters
        tag_param = request.GET.get("tag")
        category_param = request.GET.get("category")

        if tag_param:
            tag_ids = [int(i) for i in tag_param.split(",") if i.isdigit()]
            queryset = queryset.filter(tags__id__in=tag_ids)

        if category_param:
            category_ids = [int(i) for i in category_param.split(",") if i.isdigit()]
            queryset = queryset.filter(categories__id__in=category_ids)

        # Cooking time filter
        min_time = request.GET.get("min_time")
        max_time = request.GET.get("max_time")

        if min_time and min_time.isdigit():
            queryset = queryset.filter(cooking_time_min__gte=int(min_time))

        if max_time and max_time.isdigit():
            queryset = queryset.filter(cooking_time_min__lte=int(max_time))

        # Search filter
        search = request.GET.get("search")

        if search:
            queryset = queryset.filter(
                Q(title__icontains=search) |
                Q(description__icontains=search)
            )

        queryset = queryset.distinct()

        # Pagination
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

class CategoriesViewSet(viewsets.ModelViewSet):
    queryset = Categories.objects.all()
    serializer_class = CategoriesSerializer
    pagination_class = None

class TagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    pagination_class = None
