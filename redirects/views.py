from django.http import JsonResponse
from redirects.models import Redirect

def redirect_view(request, key):
        redirect = Redirect(key=key)
        result = redirect.get_redirect
        if  result:
            return JsonResponse(result, status=200)
        else:
            return JsonResponse({"message": f"{key} is not in cache"}, status=404)
