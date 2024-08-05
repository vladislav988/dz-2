import os
import datetime

from django.http import HttpResponse
from django.shortcuts import render, reverse


def home_view(request):
    template_name = 'app/home.html'
    # впишите правильные адреса страниц, используя
    # функцию `reverse`

    pages = {
        'Главная страница': reverse("home"),
        'Показать текущее время': 'current_time/',
        'Показать содержимое рабочей директории': 'workdir/'
    }
    
    # context и параметры render менять не нужно
    # подбробнее о них мы поговорим на следующих лекциях
    context = {
        'pages': pages
    }
    return render(request, 'app/home.html', context)


def time_view(request):

    current_time = str(datetime.datetime.now())[11:][:8]
    msg = f'Текущее время: {current_time}'
    context = {"time": msg}
    return render(request, "app/time.html", context)


def workdir_view(request):
    # по аналогии с `time_view`, напишите код,
    # который возвращает список файлов в рабочей 
    # директории


    context = {}

    for i in os.listdir():

        context[str(i)] = str(i)

    context = {"all": context}




    return render(request, "app/work_v.html", context)
    # raise NotImplemented
