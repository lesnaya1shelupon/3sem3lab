#!/usr/bin/env  python3
# -*- coding: utf-8 -*-

from moduli import say_name

if __name__ == '__main__':
    print("Введите имя и фамилию: ")
    (name, surname) = input().split()
    n = say_name(name, surname)
    n()
