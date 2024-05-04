from django.urls import path
from django.views.decorators.csrf import csrf_exempt

from . import views

urlpatterns = [
    path('authentications/', views.generate_auth),
    path('submit/', views.generate_auth, name='submit'),
]