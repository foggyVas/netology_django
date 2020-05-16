from django.http import HttpResponse
from django.shortcuts import render, reverse

import os
from datetime import datetime
from django.conf import settings

def info_view(request):
    msg = f'Contact email: {settings.CONTACT_EMAIL}'
    return HttpResponse(msg)


def hello_view(request):
    name = request.GET.get('name', 'SomeOne')
    page = int(request.GET.get('page', 1))
    msg = f'Hello, {name} / {page} <br/> <a href="?name=SomeTwo">NEXT</a>'
    return HttpResponse(msg)


def since_view(request, date: datetime):
    days = (datetime.now() - date).days
    msg = f'{days} дней прошло с {date}'
    return HttpResponse(msg)


def home_view(request):
    template_name = "app/home.html"
    pages = {
        'Главная страница': reverse('home'),
        'Показать текущее время': reverse('time'),
        'Показать содержимое рабочей директории': reverse('wd')
    }

    context = {
        'pages': pages
    }
    return render(request, template_name, context)


def test_view(request):
    template_name = 'app/test.html'
    return render(request, template_name)


def time_view(request):
    current_time = datetime.now().strftime('%d.%m.%Y %H:%M:%S')
    msg = f'Текущее время: {current_time}'
    return HttpResponse(msg)


def workdir_view(request):
    template_name = 'app/wd.html'
    context = {
        'wd_list': os.listdir()
    }
    return render(request, template_name, context)

# Create your views here.
