from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def mainpage(request):
    return render(request,  'mainpage.html')

def calc_home(request):
    return render(request, 'calc.html')

def travelo_home(request):
    return render(request, 'index.html')