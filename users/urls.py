from . import views
from django.urls import path
from users.views import status

urlpatterns = [
    path('status/', status),
]
