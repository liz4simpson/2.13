#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def select_train(trains, p_n):
    """
    Выбрать поезд с заданным пунктом назначения.
    """
    # Сформировать список поездок.
    result = []
    for train in trains:
        if train.get('name') == p_n:
            result.append(train)
    # Вернуть список выбранных поездов
    return result
