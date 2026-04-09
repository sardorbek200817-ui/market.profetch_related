from django.shortcuts import render , redirect
from ombor.models import Product , Category


def ombor(request):
    

    products = Product.objects.all()
    context = {
        'product':products,
    }

    return render(request , "ombor/ombor.html" , context)


def product_detail(request , product_id):
    product = Product.objects.get(id=product_id)

    return render(request , 'ombor/product_detail.html' , {'product':product})


def product_delate(request , id):

    product_delate = Product.objects.get(id=id)

    product_delate.delete()

    return redirect('ombor')



def product_update(request , id):

    product = Product.objects.get(id=id)

    if request.method == 'POST':
        name = request.POST.get('name')
        image = request.FILES.get('image')
        unit = request.POST.get('unit')
        amount = request.POST.get('amount')


        product.name = name
        product.img = image
        product.unit = unit
        product.amout = amount

        product.save()

        return redirect('product_detail' , id)

        
    elif request.method == "GET":
        return render(request , 'ombor/product_update.html' , {'product':product})
