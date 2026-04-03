from django.urls import path
from ombor.views import ombor
urlpatterns = [
    path('' , ombor, name='ombor'),
]



