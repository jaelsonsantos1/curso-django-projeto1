# from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render


# HTTP Request
def home(request):
    # return HTTP Response
    return render(request, 'recipies/home.html', context={
        'name': 'Jaelson'
    })


def sobre(request):
    # return HTTP Response
    return render(request, 'me-apague/temp.html')


def contato(request):
    # return HTTP Response
    return HttpResponse('Contato')
