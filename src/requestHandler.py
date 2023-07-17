from django.core.cache import cache
from django.http import JsonResponse, HttpRequest
from django.views.decorators.csrf import csrf_exempt
from datetime import datetime, timedelta

@csrf_exempt
def handle_post(request: HttpRequest) -> JsonResponse:
    if request.method == 'POST':
        module_root: str = request.POST.get('module_root')
        fpath: str = request.POST.get('fpath')
        cache_root: str = request.POST.get('cache_root')

        # Combine module_root and fpath to form srcPath
        src_path: str = f"{module_root}/{fpath}"

        # Check the cache for an existing entry
        cached_data: dict = cache.get(src_path)
        if cached_data is not None:
            # If an entry exists, return the cachePath
            return JsonResponse({'status': 'success','cachePath': cached_data['cachePath']})

        # If no entry exists, create a new one

        # Combine cache_root and fpath to form cachePath
        cache_path: str = f"{cache_root}/{fpath}"
        
        # Create a dictionary to store in the cache
        # Use the current time plus some TTL for the timestamp
        TTL = timedelta(minutes=5)  # TTL can be adjusted as needed
        data: dict = {
            'srcPath': src_path,
            'cachePath': cache_path,
            'timeStamp': int((datetime.now() + TTL).timestamp())
        }

        # Set the cache key to the data dictionary
        cache.set(src_path, data)

        return JsonResponse({'status': 'success', 'cachePath': cache_path})
    else:
        return JsonResponse({'status': 'invalid request'}, status=400)
