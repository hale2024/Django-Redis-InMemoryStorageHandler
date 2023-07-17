from django.shortcuts import render
from .models import *
from django.conf import settings
from django.core.cache.backends.base import DEFAULT_TIMEOUT
from django.views.decorators.cache import cache_page
from django.core.cache import cache
from datetime import datetime, timedelta
import redis

def print_cache_contents():
    r = redis.Redis(host='localhost', port=6379, db=1)
    for key in r.scan_iter():  # Iterates over keys in current selected database
        # print(f'{key.decode("utf-8")}: {r.get(key)}')
         print(key.decode("utf-8"))

CACHE_TTL = getattr(settings ,'CACHE_TTL' , DEFAULT_TIMEOUT)

def get_recipe(filter_recipe = None):
    if filter_recipe:
        print("DATA COMING FROM DB")
        
        recipes = Recipe.objects.filter(name__contains = filter_recipe)
    else:
        recipes = Recipe.objects.all()
    return recipes


def home(request):
    
    filter_recipe = request.GET.get('recipe')
    if cache.get(filter_recipe):
        print("DATA COMING FROM CACHE")
        recipe = cache.get(filter_recipe)
    else:
        if filter_recipe:
            recipe = get_recipe(filter_recipe)
            # print(filter_recipe)
            
            cache.set(filter_recipe, recipe)
        else:
            recipe = get_recipe()
    # print (request)
    context = {'recipe': recipe}
    
    return render(request, 'home.html' , context)

def show(request , id):
    if cache.get(id):
        print("DATA COMING FROM CACHE")
        recipe = cache.get(id)
    else:
        print("DATA COMING FROM DB")
        recipe = Recipe.objects.get(id = id)
        new_time = datetime.now() + timedelta(seconds=60) #the modifications i wanna make
        recipe.timeStamp = int(new_time.timestamp())
        recipe.save()
        cache.set(id , recipe)
    # print(id)
    context = {'recipe' : recipe}
    
    # clean_cache_task()
    # print("hale")
    # print_cache_contents()
    # print(cache)
    return render(request, 'show.html' , context)