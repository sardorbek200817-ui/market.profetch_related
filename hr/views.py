from django.shortcuts import render
from hr.models import Workers

def hr(request):
    hodimlar = Workers.objects.all()

    return render(request ,'hr/hr.html' , {'hodimlar':hodimlar})


