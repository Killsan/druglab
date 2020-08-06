from django.urls import path 
from . import views 

app_name = 'indx'
urlpatterns = [
    path('', views.index, name='index'),
    path('registration/', views.registration, name='registration'),
    path('login/', views.login, name='login'),
    path('account/', views.account, name='account'),
    path('account/shop/', views.shop, name='shop'),
]