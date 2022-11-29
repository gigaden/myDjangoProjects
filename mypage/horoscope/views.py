from django.http import HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render

# Create your views here.

zodiac_dict = {
    'aries': 'Знак зодиака Овен',
    'taurus': 'Знак зодиака Телец',
    'gemini': 'Знак зодиака Близнецы',
    'cancer': 'Знак зодиака Рак',
    'leo': 'Знак зодиака Лев',
    'virgo': 'Знак зодиака Дева',
    'libra': 'Знак зодиака Весы',
    'scorpio': 'Знак зодиака Скорпион',
    'sagittarius': 'Знак зодиака Стрелец',
    'capricorn': 'Знак зодиака Козерог',
    'aquarius': 'Знак зодиака Водолей',
    'pisces': 'Знак зодиака Рыбы',
}


def index(request):
    zodiacs = list(zodiac_dict)
    # li_elements += f'<li><a href = "{redirect_path}">{sign.title()}</a></li>'
    context = {'zodiacs': zodiacs}
    return render(request, 'horoscope/index.html', context)


def get_info_about_sign_zodiac(request, sign_zodiac: str):
    zodiacs = list(zodiac_dict)
    description = zodiac_dict.get(sign_zodiac)
    data = {
        'description_zodiac': description,
        'sign': sign_zodiac,
        'zodiacs': zodiacs,
        'description': description.split()[-1],

    }
    return render(request, 'horoscope/info_zodiac.html', context=data)


def get_info_about_sign_zodiac_by_number(request, sign_zodiac: int):
    zodiacs = tuple(zodiac_dict)
    if not 0 < sign_zodiac <= len(zodiacs):
        return HttpResponseNotFound('Неправильный номер знака зодиака')
    zodiac_name = zodiacs[sign_zodiac - 1]
    redirect_url = reverse('horoscope_name', args=(zodiac_name,))
    return HttpResponseRedirect(redirect_url)
