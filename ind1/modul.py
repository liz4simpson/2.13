#!/usr/bin/env python3
# _*_ coding: utf-8 _*_

def surname(s):
    def name(n):
        a = 'Уважаемая, {} {}! ' \
            'Вы делаете работу по замыканиям функций.'.format(s, n)
        return a
    return name
