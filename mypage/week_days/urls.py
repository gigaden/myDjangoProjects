from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('<int:week_day>', views.get_info_about_day_by_number),
    path('<str:week_day>', views.get_info_about_day, name = 'day_name'),
]