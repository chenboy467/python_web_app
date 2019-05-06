from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('coolWebsites/', views.coolWebsites, name='coolWebsites'),
    path('nameForm/', views.name_form, name='nameForm'),
    path('login/', views.login, name='login'),
    path('signup/', views.login, name='signup'),
    path('greet/', views.greet, name='greet'),
    path('signupresult/', views.signupresult, name='signupresult'),
    path('home/', views.home, name='home')
]
