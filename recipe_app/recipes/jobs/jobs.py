# cron.py
import random
import logging
from datetime import date

from recipes.models import DailyRecipe, Recipe

logger = logging.getLogger()


def gen_day_recipes():
    today = date.today()

    # Check if already generated today
    if DailyRecipe.objects.filter(date=today).exists():
        print(f"Daily recipes for {today} already exist")
        return

    recipes = list(Recipe.objects.all())
    random.shuffle(recipes)
    selected = recipes[:3]

    print(f"Selected recipes for {today}: {[r.id for r in selected]}")

    try:
        for recipe in selected:
            DailyRecipe.objects.create(date=today, recipe=recipe)
            print(f"Created DailyRecipe: date={today}, recipe_id={recipe.id}")
    except Exception as e:
        print(f"Error creating DailyRecipe for {today}: {e}")
        return

    print(f"Daily recipes for {today} successfully generated.")


