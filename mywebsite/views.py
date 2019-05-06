from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def home(request):
    # return HttpResponse('Here is my Response')
    return render(request, 'homepage/home.html')
