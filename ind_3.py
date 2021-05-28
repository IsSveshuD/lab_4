#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#Одноклеточная амеба каждые три часа делится на 2 клетки. Определить, сколько будет
# клеток через 6 часов.
import math

print("Сколько часов прошло?")
a = float(input())
print (math.pow(2, a//3))