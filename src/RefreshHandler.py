from background_task import background
from django.core.cache import cache
from datetime import datetime
import time

# the schedule part is the maximum limit of time that the clean_cache_task can run
#time.sleep(25) specifies the time that the clean_cache_task will wait before running
@background(schedule=120)  
def clean_cache_task(howLongToWaitInSec: int = 25) -> None:
    time.sleep(howLongToWaitInSec)
    for key in cache.iter_keys('*'):  # Redis allows for key pattern matching
        cached_data = cache.get(key)
        if cached_data['timeStamp'] < int(datetime.now().timestamp()):
                cache.delete(key)
    print("Cache cleaned")

# The clean cache function is called in the src\apps.py file
