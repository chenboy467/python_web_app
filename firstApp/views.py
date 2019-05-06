from django.shortcuts import render
from django.http import HttpResponse
from.models import Person, LoginCredential

# Create your views here.


def index(request):
    # return HttpResponse('Here is my Response')
    return render(request, 'firstApp/index.html')


def about(request):
    return render(request, 'firstApp/about.html')


def coolWebsites(request):
    data_dict = {}
    websites = []
    websites.append(['Google', 'https://www.google.com'])
    websites.append(['Amazon', 'https://www.amazon.com'])
    websites.append(['YouTube', 'https://www.youtube.com'])
    data_dict['websites'] = websites
    return render(request, 'firstApp/coolWebsites.html', data_dict)


def name_form(request):
    persons = Person.objects.all()
    data_dict = {}
    data_dict['persons'] = persons
    return render(request, 'firstApp/form.html', data_dict)


def login(request):
    return render(request, 'firstApp/login.html')


def signup(request):
    return render(request, 'firstApp/signup.html')


def greet(request):
    first_name = request.POST.get('fname')
    last_name = request.POST.get('lname')
    username = request.POST.get('username')
    password = request.POST.get('password')
    data_dict = {}
    data_dict['firstname'] = first_name
    data_dict['lastname'] = last_name
    data_dict['username'] = username
    data_dict['password'] = password
    credentials = LoginCredential.objects.all()
    for each in credentials:
        if username == each.username and password == each.password:
            data_dict['greetPewds'] = 'Hello, ' + each.firstname
        else:
            data_dict['greetPewds'] = 'YOU ARE A SPY!!!'
    data_dict['credentials'] = credentials
    return render(request, 'firstApp/greet.html', data_dict)


def signupresult(request):
    new_first_name = request.POST.get('newfirstname')
    new_last_name = request.POST.get('newfirstname')
    new_username = request.POST.get('newusername')
    new_password = request.POST.get('newpassword')
    q = LoginCredential(firstname=new_first_name, lastname=new_last_name,
                        username=new_username, password=password)
    q.save()
    return render(request, 'firstApp/greet.html', data_dict)


def home(request):
    # return HttpResponse('Here is my Response')
    return render(request, 'homepage/home.html')
