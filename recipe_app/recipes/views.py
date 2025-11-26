from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import viewsets, status

from .models import DailyRecipe, Recipe, Categories, Tag
from .serializers import RecipeSerializer, CategoriesSerializer, TagSerializer


class RecipeViewSet(viewsets.ModelViewSet):
    queryset = Recipe.objects.filter(is_published=True)
    serializer_class = RecipeSerializer

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
        from .serializers import RecipeStepSerializer
        serializer = RecipeStepSerializer(steps, many=True)
        return Response(serializer.data)

class CategoriesViewSet(viewsets.ModelViewSet):
    queryset = Categories.objects.all()
    serializer_class = CategoriesSerializer

class TagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
