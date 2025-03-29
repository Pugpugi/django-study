from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
# takes request and returns response
# request handler

# def  say_hello(request):
#     return HttpResponse('Hello world')

def calculate():
    x = 1
    y = 2
    return x


def say_hello(request):
    x = calculate()
    y = 2
    return render(request, 'hello.html', {'name': 'Mahin'})  