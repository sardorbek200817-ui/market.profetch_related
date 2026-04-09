from django.shortcuts import render
from hr.models import Workers

def hr(request):
    hodimlar = Workers.objects.all()

    return render(request ,'hr/hr.html' , {'hodimlar':hodimlar})



def hr_1(request , id):
    hr = Workers.objects.get(id=id)
    return render(request , 'hr/hr_detail.html' , {'hr':hr})

