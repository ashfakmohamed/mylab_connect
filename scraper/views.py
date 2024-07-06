from django.http import HttpResponse
from .scraper1 import scrape_shoes

def run_scraper(request):
    scrape_shoes()
    return HttpResponse("Scraping completed and data saved to shoes.csv")
    # return HttpResponse("New Scraping completed and data saved to shoes.csv")


