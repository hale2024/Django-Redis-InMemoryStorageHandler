from django.apps import AppConfig
import time
class SrcConfig(AppConfig):
    name = 'src'
    
    def ready(self):
        from .refreshHandler import clean_cache_task
        clean_cache_task(25)