from background_task import background
from django.core.cache import cache
from .models import Recipe
from datetime import datetime
import time

# the schedule part is the maximum limit of time that the clean_cache_task can run
#time.sleep(25) specifies the time that the clean_cache_task will wait before running
@background(schedule=120)  # Schedule to run every 2 minutes
def clean_cache_task(howLongToWaitInSec=25):
    time.sleep(howLongToWaitInSec)
    for key in cache.iter_keys('*'):  # Redis allows for key pattern matching
        recipe = cache.get(key)
        if isinstance(recipe, Recipe):
            if recipe.timeStamp < int(datetime.now().timestamp()):
                cache.delete(key)
    print("Cache cleaned")
