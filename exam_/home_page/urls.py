from django.urls import path
from .views import mycar_list
from . import views

urlpatterns = [
    path('', views.home_page, name='home_page'),
    path('mycar/', views.my_list, name='my_list'),
    path('mainpage/details/<int:id>', views.details, name='details'),

]