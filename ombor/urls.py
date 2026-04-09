from django.urls import path
from ombor.views import ombor , product_detail , product_delate , product_update

urlpatterns = [
    path('' , ombor, name='ombor'),
    path("detail/<int:product_id>" , product_detail , name='product_detail'),
    path('delated/<int:id>' , product_delate , name='product_delate'),
    path('update/<int:id>' , product_update , name='product_update'),
]





