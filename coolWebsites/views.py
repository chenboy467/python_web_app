from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def index(request):
    # return HttpResponse('Here is my Response')
    return render(request, 'coolWebsites/index.html')


def about(request):
    data_dict = {}
    websites = []
    websites.append(['Google', 'www.google.com'])
    websites.append(['Amazon', 'www.amazon.com'])
    websites.append(['YouTube', 'www.youtube.com'])
    data_dict['websites'] = websites
    return render(request, 'coolWebsites/about.html', data_dict)
