# from django.http import HttpResponse
from django.shortcuts import render


# HTTP Request
def home(request):
    # return HTTP Response
    return render(request, 'recipies/home.html', status=201, context={
        "name": "Jaelson"
    })
