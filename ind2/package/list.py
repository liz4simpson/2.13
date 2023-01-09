#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def display_train(trains):
    """
    Отобразить список поездов.
    """
    # Проверить, что список поездов не пуст.
    if trains:
        # Заголовок таблицы.
        line = '+-{}-+-{}-+-{}-+-{}-+'.format(
            '-' * 4,
            '-' * 30,
            '-' * 20,
            '-' * 20
        )
        print(line)
        print(
            '| {:^4} | {:^30} | {:^20} | {:^20} |'.format(
                "№",
                "Пункт назначения",
                "Номер поезда",
                "Время отправления"
            )
        )
        print(line)

        # Вывести данные о всех поездах.
        for idx, train in enumerate(trains, 1):
            time = train.get('time', '')
            print(
                '| {:>4} | {:<30} | {:<20} | {}{:>12} |'.format(
                    idx,
                    train.get('name', ''),
                    train.get('number', ''),
                    time,
                    ' ' * 5
                )
            )
            print(line)

    else:
        print('Список поездов пуст')
