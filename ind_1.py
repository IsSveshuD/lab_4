#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#С клавиатуры вводится цифра (от 1 до 12). Вывести на экран название месяца,соответствующего цифре

import sys


if __name__ == '__main__':
    n = int(input("Введите номер месяца: "))

    if n == 1:
        print("Январь")
    elif n == 2:
        print("Февраль")
    elif n == 3:
        print("Март")
    elif n == 4:
        print("Апрель")
    elif n == 5:
        print("Май")
    elif n == 6:
        print("Июнь")
    elif n == 7:
        print("Июль")
    elif n == 8:
        print("Август")
    elif n == 9:
        print("Сентябрь")
    elif n == 10:
        print("Октябрь")
    elif n == 11:
        print("Ноябрь")
    elif n == 12:
        print("Декабрь")
    else:
        print("Ошибка!", file=sys.stderr)
        exit(1)
