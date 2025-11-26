from django.db import models





# Recipes model implementation
class Recipe(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100, unique=True, null=False, db_index=True)
    description = models.TextField(null=True, blank=True)
    instructions = models.TextField(null=True, blank=True)
    cooking_time_min = models.IntegerField(null=False)

    creation_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)

    is_published = models.BooleanField(default=False, db_index=True)

    image = models.ImageField(upload_to='recipe_images/', null=True, blank=True)


    categories = models.ManyToManyField("Categories", through="RecipeCategories")
    tags = models.ManyToManyField("Tag", through="RecipeTags")

    def __str__(self):
        return f'{self.id} - {self.title}'

# Steps model implementation
class RecipeStep(models.Model):
    id = models.AutoField(primary_key=True)
    recipe_id = models.ForeignKey('Recipe', on_delete=models.CASCADE, null=False)
    step_number = models.IntegerField(null=False, db_index=True)
    instruction = models.TextField(max_length=100, null=False)

    def __str__(self):
        return f'{self.recipe_id} - Step {self.step_number}'

# Categories model implementation
class RecipeCategories(models.Model):
    id = models.AutoField(primary_key=True)
    recipe_id = models.ForeignKey('Recipe', on_delete=models.CASCADE, null=False, related_name='category_links')
    category_id = models.ForeignKey('Categories', on_delete=models.CASCADE, null=False, related_name='recipe_links')

    def __str__(self):
        return f'{self.id} - {self.category_id}'


class Categories(models.Model):
    id = models.AutoField(primary_key=True)
    category_name = models.CharField(max_length=50, unique=True, null=False, db_index=True)

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"

    def __str__(self):
        return f'{self.id} - {self.category_name}'


# Recipe model implementation
class RecipeTags(models.Model):
    id = models.AutoField(primary_key=True)
    recipe_id = models.ForeignKey('Recipe', on_delete=models.CASCADE, null=False, related_name='tag_links')
    tag_id = models.ForeignKey('Tag', on_delete=models.CASCADE, null=False, related_name='recipe_links')

    def __str__(self):
        return f'{self.recipe_id} - {self.tag_id}'


class Tag(models.Model):
    id = models.AutoField(primary_key=True)
    tag_name = models.CharField(max_length=50, unique=True, null=False, db_index=True)

    def __str__(self):
        return self.tag_name


# DailyRecipe model implementation
class DailyRecipe(models.Model):
    id = models.AutoField(primary_key=True)
    date = models.DateField(db_index=True, null=False)
    recipe = models.ForeignKey('Recipe', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.date}: {self.recipe.id} - {self.recipe.title}"
