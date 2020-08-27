from django.urls import path 
from . import views 

app_name = 'indx'
urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.loginPage, name='login'),
    path('logout/', views.logoutUser, name='logout'),
    path('registration/', views.registrationPage, name='registration'),
    path('create/', views.create_main, name='create'),
    # path('user/', views.userPage, name='userPage'),
]