from django.urls import path
from hr.views import hr

urlpatterns = [
    path('' ,hr , name='hr'),
]




