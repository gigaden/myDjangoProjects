from . import views
from django.urls import include, path

urlpatterns = [
    path('', views.show_all_movie, name='index'),
    path('movie/<slug:slug_movie>', views.show_one_movie, name='movie_detail'),
    path('__debug__/', include('debug_toolbar.urls')),
]
