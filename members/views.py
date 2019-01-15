from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime


def home(request):
    return HttpResponse("Hello, Django!")


def hello_there(request, name):
    return render(
        request,
        'members/hello_there.html',
        {
            'name': name,
            'date': datetime.now()
        }
    )
