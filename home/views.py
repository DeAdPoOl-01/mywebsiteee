from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    # return HttpResponse('Hello Django!')
    return render(request,'index.html')

def index(request):
    return HttpResponse('About us')

def contact(request):
    return HttpResponse('Contact page')