#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
from package.add import get_train
from package.help import help
from package.list import display_train
from package.select import select_train


def main():
    """
    Главная функция программы.
    """
    # Список поездов.
    trains = []

    # Организовать бесконечный цикл запроса команд.
    while True:
        # Запросить команду из терминала.
        command = input(">>> ").lower()

        # Выполнить действие в соответствие с командой.
        if command == 'exit':
            break

        elif command == 'add':
            # Запросить данные о поездке.
            train = get_train()

            # Добавить словарь в список.
            trains.append(train)
            if len(trains) > 1:
                # Сортировка
                trains.sort(key=lambda item: item.get('time', ''))

        elif command == 'list':
            # Отобразить все поезда.
            display_train(trains)

        elif command.startswith('select'):
            parts = command.split(' ', maxsplit=1)
            # Получить требуемый пункт назначения.
            p_n = str(parts[1])
            # Выбрать поезда с заданным пунктом назначения.
            selected = select_train(trains, p_n)
            # Отобразить выбранные поезда
            display_train(selected)

        elif command == 'help':
            # Вывести справку о работе с программой.
            help()
        else:
            print(f"Неизвестная команда {command}", file=sys.stderr)


if __name__ == '__main__':
    main()
