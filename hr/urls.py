from django.urls import path
from hr.views import hr , hr_1

urlpatterns = [
    path('' ,hr , name='hr'),
    path('/hr_1/<int:id>' , hr_1 , name="hr_1"),
]




