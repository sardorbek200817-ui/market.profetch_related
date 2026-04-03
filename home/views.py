from django.shortcuts import render
from hr.models import Workers , Salary
from ombor.models import Category , Product


def home(request):
    hodimlar = Workers.objects.all().count()
    mahsulotlar = Product.objects.all().count()
    context = {
        'hodimlar':hodimlar,
        'mahsulotlar':mahsulotlar,
    }

    return render(request ,'home.html' , context)

















    