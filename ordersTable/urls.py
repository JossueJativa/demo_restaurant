from django.urls import path
from . import views

app_name = 'ordersTable'

urlpatterns = [
    path('', views.index, name='index'),
]