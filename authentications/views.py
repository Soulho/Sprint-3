from django.http import JsonResponse
from .logic.logic_auth import get_auths
import random
from django.http import HttpResponse

def auth_list(request):
    auths = get_auths()
    context = list(auths.values())
    return JsonResponse(context, safe=False)

def generate_auth(request):
    
    code = random.randint(1000,9999)
    return HttpResponse("El código de autenticación es: "+ str(code))

   
