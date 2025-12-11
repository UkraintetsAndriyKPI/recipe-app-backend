# Recipe App Backend

**Recipe App Backend** is a RESTful API built with **Django REST Framework** for managing recipes. It serves as the backend for an Android recipe application, providing endpoints for recipes, categories, tags, daily recommendations, and filtering functionality.

## Features

- **Recipe Management**: CRUD operations for recipes.
- **Daily Recipes**: Retrieve the last 3 daily recommended recipes.
- **Ingredients & Steps**: Access detailed recipe steps and ingredients.
- **Filtering**: Filter recipes by tags, categories, cooking time, and search queries.
- **Admin Access**: Staff users can view unpublished recipes.

## Tech Stack

- **Python 3.11+**
- **Django 5.2.7**
- **Django REST Framework 3.16.1**
- **drf-yasg** for API documentation
- **APScheduler** for scheduled tasks
- **SQLite / PostgreSQL** for database
