from django.urls import path
from .views import run_scraper

urlpatterns = [
    path('scraper_app/', run_scraper),
]
