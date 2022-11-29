from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render

# Create your views here.
days_dict = {'monday': 'Список дел на понедельник', 'tuesday': 'Список дел на вторник',
             'wednesday': 'Список дел на среду', 'thursday': 'Список дел на четверг',
             'friday': 'Список дел на пятницу', 'saturday': 'Список дел на субботу',
             'sunday': 'Список дел на воскресенье'
             }


def index(request):
    days = tuple(days_dict)
    li_elements = ''
    for day in days:
        redirect_path = reverse('day_name', args = [day])
        li_elements += f'<li><a href ="{redirect_path}">{day.title()}</a></li>'
    response = f'''
    <ul>
        {li_elements}
    </ul>
    '''
    return HttpResponse(response)


def get_info_about_day(request, week_day: str):
    day = days_dict.get(week_day)
    if day:
        return render(request, 'week_days/greeting.html')
    else:
        return HttpResponseNotFound('Этого дня в списке нет')


def get_info_about_day_by_number(request, week_day: int):
    if not 1 <= week_day <= len(days_dict):
        return HttpResponseNotFound('Такого дня не существует')
    days = tuple(days_dict)
    days_name = days[week_day - 1]
    redirect_url = reverse('day_name', args=(days_name,))
    return HttpResponseRedirect(redirect_url)
