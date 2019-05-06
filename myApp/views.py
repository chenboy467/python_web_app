from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def index(request):
    # return HttpResponse('Here is my Response')
    things_dict = {}
    things_dict['name'] = 'Big Chungus'
    things_dict['thing1'] = 'Thing 1'
    things_dict['thing2'] = 'Thing 2'
    things_dict['thing3'] = 'Thing 3'
    things_dict['thing4'] = 'Thing 4'
    things_dict['thing5'] = 'Thing 5'
    outer_list = []
    outer_list.append(
        ['Ugandan Knuckles', '21', 'Knowing da wae', '0', '0', '-1000000'])
    outer_list.append(
        ['Big Chungus', '69', 'How 2 B BIGG', '100', 'Googleplex', 'Aleph null'])
    things_dict['outer_list'] = outer_list
    things_dict['admin'] = False
    things_dict['member'] = True
    things_dict['username'] = 'chenboy 467'
    return render(request, 'myApp/index.html', things_dict)


def about(request):
    return render(request, 'myApp/about.html')


def uganda(request):
    return render(request, 'myApp/uganda.html')


def chungus(request):
    return render(request, 'myApp/chungus.html')
