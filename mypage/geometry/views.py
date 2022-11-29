from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render


# Create your views here.

def get_rectangle_area(request, width, height):
    # return HttpResponse(f'Площадь прямоугольника размером {width}x{height} = {width * height}')
    return render(request, 'geometry/rectangle.html')


def get_square_area(request, width):
    # return HttpResponse(f'Площадь квадрата размером {width} x {width} = {width ** 2}')
    return render(request, 'geometry/square.html')


def get_circle_area(request, radius):
    # return HttpResponse(f'Площадь круга радиусом {radius} = {radius ** 2}')
    return render(request, 'geometry/circle.html')


def rectangle(request, width, height):
    redirect_url = reverse('rectangle_name', args=(width, height))
    return HttpResponseRedirect(redirect_url)


def square(request, width):
    redirect_url = reverse('square_name', args=(width,))
    return HttpResponseRedirect(redirect_url)


def circle(request, radius):
    redirect_url = reverse('circle_name', args=(radius,))
    return HttpResponseRedirect(redirect_url)
