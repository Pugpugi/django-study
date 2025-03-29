from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home(request):
    return render(request,  'calc.html', {'name': "Mimmy"})

def add(request):
    if request.POST['num1'] != None  and request.POST['num2'] != None:
        val1 = int(request.POST['num1'])
        val2 = int(request.POST['num2'])

    elif request.POST['num1'] == None:
        val1 = 0

    elif request.POST['num2'] == None:
        val2 = 0

    else:
        val1 = 0
        val2 = 0

    res = val1 + val2

    return render(request, "result.html", {'result':res})