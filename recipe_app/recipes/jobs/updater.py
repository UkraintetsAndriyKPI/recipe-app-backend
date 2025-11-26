from apscheduler.schedulers.background import BackgroundScheduler
from .jobs import gen_day_recipes

def start():
    scheduler = BackgroundScheduler()
    scheduler.add_job(gen_day_recipes, 'interval', min=10)
    scheduler.start()
