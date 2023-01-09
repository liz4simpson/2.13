#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import datetime


def get_train():
    """
    Запросить данные о поезде.
    """
    name = input("Пункт назначения: ")
    number = input("Номер поезда: ")
    time_str = input("Время отправления: (hh:mm) ")
    time = datetime.datetime.strptime(time_str, '%H:%M').time()

    # Создать словарь.
    return {
        'name': name,
        'number': number,
        'time': time,
    }
