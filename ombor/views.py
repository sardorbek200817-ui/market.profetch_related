from django.shortcuts import render
from ombor.models import Product , Category


def ombor(request):
    
    category = Category.objects.all()
    products = Product.objects.all()
    context = {
        'category':category,
        'product':products,
    }

    return render(request , "ombor/ombor.html" , context)










