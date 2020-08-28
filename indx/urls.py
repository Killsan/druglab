from django.urls import path 
from django.contrib import admin
from . import views 

app_name = 'indx'
urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.loginPage, name='login'),
    path('logout/', views.logoutUser, name='logout'),
    path('registration/', views.registrationPage, name='registration'),
    path('create/', views.create_main, name='create'),
    path('admin/', admin.site.urls),
    path('<bot>/', views.botInfo, name='botInfo'),
]