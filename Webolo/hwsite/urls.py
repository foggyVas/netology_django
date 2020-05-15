"""hwsite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, register_converter
from datetime import datetime

from app.views import time_view, info_view, hello_view, since_view, test_view, \
    home_view, workdir_view
from temp.views import index_view


class DateConverter:
    regex = '[0-9]{4}-[0-9]{2}-[0-9]{2}'

    def to_python(self, value: str) -> datetime:
        return datetime.strptime(value, '%Y-%m-%d')

    def to_url(self, value: datetime) -> str:
        return value.strftime('%Y-%m-%d')


register_converter(DateConverter, 'datetime')

urlpatterns = [
    path('wd/', workdir_view, name='wd'),
    path('home/', home_view, name='home'),
    path('test/', test_view, name='test'),
    path('index/', index_view, name='index'),
    path('since/<datetime:date>/', since_view, name='since'),
    path('hello/', hello_view, name='hello'),
    path('current_time/', time_view, name='time'),
    path('info/', info_view, name='info'),
    path('admin/', admin.site.urls),
]
